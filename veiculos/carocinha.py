from grafo.vertice import Vertice
from grafo.grafo import Grafo
from extras.settings import *
from .veiculo import Veiculo

class Carrocinha(Veiculo):
    def __init__(self, pos:int):
        super().__init__(pos)

    def cheio(self):
        return self.carga == MAX_CARROCINHA_CARGA


    def coletar(self, g:Grafo):
        v:Vertice = g.vertices[self.caminho[0]]
        livre = MAX_CARROCINHA_CARGA - self.carga

        if v.cachorro:                                                      # Coleta animais e atualiza valores pros diferentes casos
            self.carga += v.cachorro if livre >= v.cachorro else livre
            v.cachorro = 0 if livre >= v.cachorro else v.cachorro - livre
        if v.gato:
            self.carga += v.gato if livre >= v.gato else livre
            v.gato = 0 if livre >= v.gato else v.gato - livre

    
    def __str__(self):
        return f"animais: {self.carga}\ncaminho: {self.caminho}\nestado: {self.estado}"
