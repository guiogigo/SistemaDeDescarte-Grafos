from random import *

class Vertice:
    def __init__(self,n):                                   # Construtor do Vértice
        self.n = n
        self.lixo = randint(0,10)                           # Adiciona lixo e animais no momento de criação
        self.rato = 1 if randint(1,2) == 1 else 0           
        self.gato = 1 if randint(1,4) == 1 else 0
        self.cachorro = 1 if randint(1,10) == 1 else 0
    
    def __str__(self):                                      # Põe suas informações em formato de string se chamar print(vertice)
        return f"v={self.n}, l={self.lixo}, r={self.rato}, g={self.gato}, c={self.cachorro}" 
    
    def get_Lixo(self):
        return self.lixo
    
    def set_Lixo(self, num: int):
        self.lixo = num