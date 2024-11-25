from grafo import Grafo
from heapq import *

def caminhoMin(vi:int,vf:int,g:Grafo) -> list[int]:
    H = []
    C = [int]*g.qtd
    pai = [int]*g.qtd
    visitados = []
    caminho = []


    for i in range(g.qtd):
        pai[i] = i
        C[i] = float('inf') if i != vi else 0
        heappush(H,(C[i],i))

    while len(H):
        u = heappop(H)[1]
        if u not in visitados:
            visitados.append(u)

            for z in g.adjacencias[u]:
                if C[z] > C[u] + g.pesos[u][z]:
                    C[z] = C[u] + g.pesos[u][z]

                    heappush(H,(C[z],z))
                    pai[z] = u
            if u == vf:
                break
    
    i = vf
    print(f"caminho de {vi} para {i}")
    while i != pai[i]:
        caminho.insert(0,i)
        i = pai[i]
    caminho.insert(0,i)
    return caminho
