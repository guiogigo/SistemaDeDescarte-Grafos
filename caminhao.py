from vertice import Vertice
from grafo import Grafo
from settings import *

class Caminhao:
    def __init__(self, pos:int, funcionarios:int):
        self.funcionarios = funcionarios
        self.lixo = 0
        self.caminho = [pos]    # indice 0 é o vértice atual
        self.retornando = False
    
    def cheio(self):
        return self.lixo == MAX_CAMINHAO_CARGA

    def coletar(self, g:Grafo):
        
        v:Vertice = g.vertices[self.caminho[0]]
        qtd = MAX_CAMINHAO_CARGA - self.lixo
        if qtd >= v.lixo:               # Se a capacidade do caminhão for maior que o vértice
            lixo = v.lixo            
            v.lixo = 0                  # Esvazia totalmente e retorna a quantidade de lixo que tinha no vértice
            if v.n in g.verticesCheios:
                g.verticesCheios.remove(v.n)
            self.lixo += lixo
            return lixo//self.funcionarios
        
        v.lixo -= qtd                   # Senão subtrai por qtd e retorna esse qtd
        self.lixo += qtd
        return qtd//self.funcionarios
    

    def mover(self,g:Grafo):
        return g.pesos[self.caminho.pop(0)][self.caminho[0]]