from grafo.grafo import Grafo
from veiculos.caminhao import Caminhao
from veiculos.carocinha import Carrocinha
from random import choice
from extras.algoritmos import *
from extras.settings import *

from json import *


#-----------------------------------------
with open("grafo.json", "r") as file:
    arqGrafo = load(file)

# Criação do grafo
g = Grafo(arqGrafo["pontos"],arqGrafo["direcionado"])

for v in g.vertices:
    v.encher()

for j in range(len(arqGrafo["arestas"])):
    g.add_aresta(arqGrafo["arestas"][j][0], arqGrafo["arestas"][j][1], arqGrafo["arestas"][j][2])

print(g)

lixao = arqGrafo["aterro"]
zoo = arqGrafo["centroZoo"]

#--------------------------------------------
# Inico do loop de simulação


qtdCaminhoes = 1
qtdFuncionarios = MIN_CAMINHAO_FUNCIONARIOS-1

tempo = [MAX_TEMPO+1]

while max(tempo) > MAX_TEMPO:

    for v in g.vertices:
        v.encher()
    g.verticesCheios = [i for i in range(g.qtd)]
    carrocinhas = [Carrocinha(zoo) for _ in range(QTD_CARROCINHA)]

    qtdFuncionarios += 1
    if qtdFuncionarios%5 == 1:
        qtdCaminhoes += 1
        qtdFuncionarios = MIN_CAMINHAO_FUNCIONARIOS*qtdCaminhoes
    
    caminhoes:list[Caminhao] = []
    f = qtdFuncionarios
    for i in range(qtdCaminhoes):
        caminhoes.append(Caminhao(lixao,round(f//(qtdCaminhoes-i))))
        f -= f//qtdCaminhoes

    destCarrocinha = []
    
    tempo = [0]*qtdCaminhoes
    while len(g.verticesCheios)>0 and max(tempo) < MAX_TEMPO:

        for i in range(g.qtd):
            adj = [g.vertices[v] for v in g.adjacencias[i]]
            g.vertices[i].moverAnimal(adj)

        for i,c in enumerate(caminhoes):                                # Para cada caminhão
            if len(c.caminho)==1:                                       # Se o caminho anterior ja foi percorrido
                try:
                    dest = choice(g.verticesCheios)
                except:
                    dest = lixao
                while dest == c.caminho[0] and len(g.verticesCheios)>1:
                    dest = choice(g.verticesCheios)
                c.caminho = caminhoMin(c.caminho[0],dest,g)             # Cria um novo caminho para um vértice cheio aleatório 
            

            if c.caminho[0] in g.verticesCheios and not c.cheio():
                    tempo[i] += c.coletar(g) * (2 if g.vertices[c.caminho[0]].temAnimal() != 'vazio' else 1)  # coleta e calcula o tempo
            
            if c.cheio() and c.estado == 'indo':
                c.estado = 'voltando'
                c.caminho = caminhoMin(c.caminho[0],lixao,g)            # Se ficou cheio, cria um caminho de volta pro lixao
                

            if g.vertices[c.caminho[0]].temAnimal() == 'geral' and c.caminho[0] not in destCarrocinha:     # Se encontrou animal em um vértice novo, poe na lista pra carrocinha
                destCarrocinha.append(c.caminho[0])
            
            
            if c.caminho[0] == lixao and c.estado == 'voltando':   # Se chegar no lixao, esvazia e atualiza estado
                c.esvaziarCaminhao()
            
            print(f"=== Caminhão {i} ===\n{c}\n")
            if len(c.caminho)>1:        # Move o caminhao se o caminho tem 2+ vértices
                tempo[i] += c.mover(g)
        

        for i,c in enumerate(carrocinhas):                      # Para cada carrocinha

            for v in destCarrocinha:                            # Se algum vértice na fila já está no caminho de algum carro, remover ele
                if v in c.caminho:
                    destCarrocinha.remove(v)
            

            if c.estado == 'parado' and len(destCarrocinha)>0:          # Acionar a carrocinha se algum ponto entrar na fila
                c.estado = 'indo'
                c.caminho = caminhoMin(zoo,destCarrocinha.pop(0),g)
                for v in [x for x in c.caminho if x in destCarrocinha]: # Remover ponto da fila se o caminho ja passa por ele
                    destCarrocinha.remove(v)
            

            if g.vertices[c.caminho[0]].temAnimal() and not c.cheio():        # Se tem animal, coleta
                c.coletar(g)
            

            if c.estado == 'indo' and (len(c.caminho)==1 or c.cheio()):     # Se encher ou chegou no destino, volta pra base
                c.estado = 'voltando'
                c.caminho = caminhoMin(c.caminho[0],zoo,g)
            

            print(f"--- Carrocinha {i} ---\n{c}\n") if c.estado != 'parado' else None
            if len(c.caminho)>1 and c.estado != 'parado':           # Mover se o caminho tem 2+ vertices
                c.mover(g)
            

            if c.caminho[0] == zoo and c.estado == 'voltando':      # Esvaziar carro se chegou na base
                c.carga = 0
                c.estado = 'parado'

    print("---------------------------------------------------------------------\n" 
          +f"Nº Caminhões: {qtdCaminhoes}\nNº Funcionarios: {qtdFuncionarios}\nTempo final: {max(tempo)} min\n"
          +"---------------------------------------------------------------------\n" )