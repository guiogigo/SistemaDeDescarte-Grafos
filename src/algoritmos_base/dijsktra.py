import heapq
from grafo import grafo

def dijsktra(g: grafo.Grafo, v, n):
    H = []
    C = []
    for i in range(0, n):
        C.append(g.get_peso(v, i))    
        heapq.heappush(H, (C[i], i))
    
    visitados = set()
    while len(H) != 0:
        print(H)
        u = heapq.heappop(H)
        if(u[1] in visitados): continue
        
        visitados.add(u[1])
        print(f"Escolhido: {u}")
        for z in g.get_adjacensias(u[1]):
            print(f"Vizinho: {z}")
            if C[u[1]] + g.get_peso(u[1], z) < C[z]:
                C[z] = C[u[1]] + g.get_peso(u[1], z)
                print("Custo alterado")
                heapq.heappush(H, (C[z], z))
    return C