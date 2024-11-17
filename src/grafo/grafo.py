from .Vertice import * 

class Grafo:
    def __init__(self, direcionado=False):                  # Construtor do Grafo
        self.vertices = {}      # Dicionario de vértices, basicamente usado como um vetor normal, porém com mais utilidades
        self.adjacencias = {}   # Dicionario de adjacencias, cada chave representa o vertice, e os itens por chave são seus vizinhos
        self.pesos = []         # Declarador da matriz de pesos
        
        self.direcionado = direcionado
    
    def add_vertices(self, qtd):            # Cria e adiciona todos os vértices automaticamente
        for i in range(qtd):
            self.vertices[i] = Vertice(i)
            self.adjacencias[i] = []
        
        self.pesos = [[0 for _ in range(qtd)] for _ in range(qtd)]  # Gera a matriz de pesos para entao colocar valores iniciais
        for i in range(qtd):                                        # (É melhor assim mesmo)
            for j in range(qtd):
                self.pesos[i][j] = float('inf') if i!=j else 0
    
    def getVertice(self, v) -> Vertice:
        return self.vertices[v]
        


    def add_aresta(self, v1, v2, peso=1):               # Adiciona as arestas no dicionario de adjacencia
        if v1 in self.vertices and v2 in self.vertices: # Se os vertices existirem no grafo:
            self.adjacencias[v1].append(v2)             # Coloca v2 como item da chave v1, v2 vizinho de v1
            self.pesos[v1][v2] = peso
            if not self.direcionado:                    # Se não for direcionado, faz a operação simétrica
                self.adjacencias[v2].append(v1)
                self.pesos[v2][v1] = peso

    def get_peso(self, v1, v2):
        return self.pesos[v1][v2]
    
    def get_adjacensias(self, v):
        return self.adjacencias[v]
        
    def buscaLarg(self,v):              # Busca em largura normal
        visitados = []
        fila = [v]
        ordem_visita = []

        while fila:
            u = fila.pop(0)
            if u not in visitados:
                visitados.append(u)
                ordem_visita.append(u)

                for v in self.adjacencias[u]:
                    if v not in visitados and v not in fila:
                        fila.append(v)
        return ordem_visita
    
    def printpeso(self):        # Só printa os pesos
        n = len(self.vertices)
        for i in range(n):
            print(f"{self.pesos[i]}")

    
    def __str__(self):              # Transforma o grafo em string
        resultado = "Grafo:\n"
        for v in self.vertices:     # Para cada chave no dicionario de vertices:
            resultado += f"{v}|"    # Coloca essa chave no inicio da linha
            for w in self.adjacencias[v]:   # Pra cada vizinho dessa chave no dicionario de adjacencia:
                resultado += f" -{self.pesos[v][w]}-> ({w})"    # Coloca todos eles depois de 'v|', separados por uma seta que mostra o peso da aresta 'vw'
            resultado += "\n"   # Nova linha
        return resultado

"""
g = Grafo()
g.add_vertices(4)

g.add_aresta(0,1,3)
g.add_aresta(1,2,2)
g.add_aresta(2,3,8)
g.add_aresta(1,3,4)


g.printpeso()
print(g)
###
"""