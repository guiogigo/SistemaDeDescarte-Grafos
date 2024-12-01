from .vertice import Vertice 

class Grafo:
    def __init__(self, qtd:int ,direcionado=False):                  # Construtor do Grafo
        self.vertices:list[Vertice] = [None]*qtd
        self.qtd = qtd
        self.verticesCheios = []
        self.adjacencias = {}      
        
        self.direcionado = direcionado

        for i in range(qtd):
            self.vertices[i] = Vertice(i)                           # Cria todos os n vertices
            self.verticesCheios.append(i)
            self.adjacencias[i] = []
        
        self.pesos = [[0 for _ in range(qtd)] for _ in range(qtd)]  # Gera a matriz de pesos para entao colocar valores iniciais
        for i in range(qtd):                                        
            for j in range(qtd):
                self.pesos[i][j] = float('inf') if i!=j else 0
        

    def add_aresta(self, v1:int, v2:int, peso=1):           # Adiciona as arestas no dicionario de adjacencia
        if 0<=v1<self.qtd and 0<=v2<self.qtd:
            self.adjacencias[v1].append(v2)                 # Coloca v2 como item da chave v1, v2 vizinho de v1
            self.pesos[v1][v2] = peso
            if not self.direcionado:                        # Se não for direcionado, faz a operação simétrica
                self.adjacencias[v2].append(v1)
                self.pesos[v2][v1] = peso

    
    def __str__(self):              # Transforma o grafo em string
        resultado = "\nGrafo:\n\n-+-----------\n"
        for v in range(self.qtd):     # Para cada chave no dicionario de vertices:
            resultado += f"{v}|"
            single = True
            for w in self.adjacencias[v]:   # Pra cada vizinho dessa chave no dicionario de adjacencia:
                resultado += f" -{self.pesos[v][w]}-> ({w})" if single else f"\n | -{self.pesos[v][w]}-> ({w})"
                single = False
            resultado += "\n-+-----------\n"
        return resultado
    
