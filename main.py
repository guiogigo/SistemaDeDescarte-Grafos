from grafo import Grafo
from vertice import Vertice
from caminhao import Caminhao
import random
from algoritmos import *


qtd = int(input("Nº vértices: "))
g = Grafo(qtd,int(input("Direcionado?: (1/0)")))

for v in g.vertices:
    v.encher()

print(g)

print("Adicione uma aresta, no formato 'v1,v2,peso'.\nPeso 0 para terminar.")

while True:
    print(g)
    print("-> ",end='')
    aresta = [int(i) for i in input().split(',')]
    
    if aresta[2]<=0:
        break

    g.add_aresta(aresta[0],aresta[1],aresta[2])

lixao = int(input("Escolha um vértice para ser o aterro: "))
zoo = int(input("Escolha um vértice para ser o Centro de Zooneses: "))


caminhoes = [Caminhao(lixao,3)]
tempo = 0
while len(g.verticesCheios)>0:
    for c in caminhoes:

        if len(c.caminho)==1:
            c.caminho = caminhoMin(c.caminho[0],random.choice(g.verticesCheios),g)
        
        if c.cheio() and not c.retornando:
            c.retornando = True
            c.caminho = caminhoMin(c.caminho[0],lixao,g)
        else:
            tempo += c.coletar(g)
        
        print("caminho do caminhao: ",c.caminho)
        if len(c.caminho)>1:
            tempo += c.mover(g)
        
        if c.caminho[0] == lixao:
            c.lixo = 0
            c.retornando = False

print(tempo)