from random import *

from settings import *

class Vertice:
    def __init__(self,n):                                   # Construtor do Vértice
        self.n = n
        self.lixo = 0                       
        self.rato = 0         
        self.gato = 0
        self.cachorro = 0
    
    def encher(self):
        self.lixo = randint(MIN_VERTICE_LIXO,MAX_VERTICE_LIXO)                           # Adiciona lixo e animais
        self.rato = 1 if randint(1,2) == 1 else 0
        self.gato = 1 if randint(1,4) == 1 else 0
        self.cachorro = 1 if randint(1,10) == 1 else 0
    

    def __str__(self):                                      # Põe suas informações em formato de string se chamar print(vertice)
        return f"v={self.n}, l={self.lixo}, r={self.rato}, g={self.gato}, c={self.cachorro}" 
    

    def temAnimal(self):
        return (self.rato or self.gato or self.cachorro)
    

    def moverAnimal(self, adjacentes:list):
        """ Rato atrai gato que atrai cachorro.
        Caso um ponto de coleta contenha ao menos um gato, então os ratos fogem para outro ponto de coleta, a menos de um que é
        vítima do gato. O mesmo ocorre caso o ponto contenha ao menos um cachorro para os gatos presentes, com exceção
        que o gato foge mais rapidamente que o cachorro para outro ponto de coleta. Caso um ponto contenha os três animais
        simultaneamente a qualquer momento, então os gatos e ratos fogem todos para pontos vizinhos, enquanto os cachorros
        permanecem no mesmo ponto. Se um ponto de coleta não possui lixo, então os animais presentes se encaminham para
        algum ponto próximo. """
        pass

