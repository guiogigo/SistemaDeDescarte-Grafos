from grafo.Grafo import Grafo
from coletorDeLixo.Caminhao import Caminhao
import heapq

g = Grafo()
truck = Caminhao()

g.add_vertices(4)

g.add_aresta(0,1,3)
g.add_aresta(1,2,2)
g.add_aresta(2,3,8)
g.add_aresta(1,3,4)

def dijsktraPai(g: Grafo, v, n):
    H = []                                  # Heap
    C = []                                  # Lista de Custos
    pai = [(None, None)] * n     
                   # Lista de pai para n vertices
    caminho = {i: [] for i in range(n)}     # Dicionário de caminhos para cada vértice
    for i in range(0, n):                       
        C.append(g.get_peso(v, i))          # Coloca os pesos na lista de custos
        heapq.heappush(H, (C[i], i))        # Coloca as tuplas (peso, vertice) no Heap

    visitados = set()                       # Lista de vertices visitados
    while len(H) != 0:                      # Enquanto tiver coisa no Heap
        #print(H)
        u = heapq.heappop(H)                # u recebe o menor do heap
        if(u[1] in visitados): continue     # se u já foi visitado pula (u[1] é o vertice da tupla u)                                           
        visitados.add(u[1])                 # Coloca o vertice u como visitado                
        #print(f"Escolhido: {u}")
        for z in g.get_adjacensias(u[1]):   # para todo z pertencente os vizinhos de u
            #print(f"Vizinho: {z}")
            if C[u[1]] + g.get_peso(u[1], z) <= C[z]:   # aqui é o calculo fodase você sabe
                C[z] = C[u[1]] + g.get_peso(u[1], z)
                #print("Custo alterado")
                heapq.heappush(H, (C[z], z))            # Coloca a tupla no heap
                pai[z] = u                         # Coloca o pai no lugar certo
    
    for i in range(0, n):                   # para todo vertice
        atual = (C[i], i)                           # pega o vertice
        while atual[1] != None:                # enquanto ele não for nulo(o vertice escolhido deve ser nulo)
            caminho[i].insert(0, atual)     # insere o pai no inicio
            atual = pai[atual[1]]              # passa pro próximo pai

    return caminho                          # FIM
"""
    [0][0]
    [1][0, 1]
    [2][0, 1, 2]
    [3][0, 1, 3]
"""

def juntar_Lixo(c: Caminhao, caminhos: dict, v: int, g: Grafo): # quero fazer uma função simples só para adicionar o lixo no camninhao ao longo do percurso
    for i in caminhos[v]:                     
        print(i) 
        c.qtd_lixo += g.getVertice(i[1]).get_Lixo()    
        print(c.qtd_lixo) 


caminhos = dijsktraPai(g, 0, 4)
for i in range(4):
    print(f"{i}: {caminhos[i]}")
juntar_Lixo(truck, caminhos, 2, g)
