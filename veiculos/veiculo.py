from grafo.grafo import Grafo

class Veiculo:
    def __init__(self,pos:int):         # Superclasse veículo para simplificar os outros
        self.carga = 0
        self.caminho = [pos]
        self.estado = 'parado'

    def mover(self,g:Grafo):
        return g.pesos[self.caminho.pop(0)][self.caminho[0]]

