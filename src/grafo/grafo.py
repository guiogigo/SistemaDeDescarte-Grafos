class Vertice:
    def __init__(self, n, lixo, rato, gato, cachorro):
        self.n = n
        self.lixo = lixo
        self.rato = rato
        self.gato = gato
        self.cachorro = cachorro

    def __str__(self):
        return f"({self.n}, l={self.lixo}, r={self.rato}, g={self.gato}, c={self.cachorro})"

class Grafo:
    def __init__(self, ponderado=False, direcionado=False):
        self.vertices = {}
        self.adjacencias = {}
        self.ponderado = ponderado
        self.direcionado = direcionado

    def add_vertice(self, n, lixo, rato, gato, cachorro):
        if n not in self.vertices:
            vertice = Vertice(n, lixo, rato, gato, cachorro)
            self.vertices[n] = vertice
            self.adjacencias[n] = []

    def add_aresta(self, n1, n2, peso=1):
        if n1 in self.vertices and n2 in self.vertices:
            if self.ponderado:
                self.adjacencias[n1].append((n2,peso))
                self.adjacencias[n2].append((n1,peso)) if not self.direcionado else None
            else:
                self.adjacencias[n1].append((n2))
                self.adjacencias[n2].append((n1)) if not self.direcionado else None
    
    def buscaLarg(self,v):
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

    """ def print(self):
        for v in self.adjacencias:
            print(f"[{self.vertices[v]}] -> ",end='')
            print(*self.adjacencias[v],sep=" -> ") """


    def __str__(self):
        resultado = "Grafo:\n"
        for n, v in self.vertices.items():
            adjacentes = [self.vertices[n_adj] for n_adj,x in self.adjacencias[n]]
            resultado += f"{v} -> {', '.join(str(adj) for adj in adjacentes)}\n"
        return resultado


# Exemplo de uso
g = Grafo(True)
g.add_vertice(1,10,1,1,1)
g.add_vertice(2,0,1,0,0)
g.add_vertice(3,5,3,2,1)
g.add_vertice(4,3,10,2,2)


g.add_aresta(1, 2)
g.add_aresta(2, 3)
g.add_aresta(2,4)
print(g.adjacencias)
print(g)