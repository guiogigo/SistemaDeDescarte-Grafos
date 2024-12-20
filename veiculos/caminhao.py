from grafo.vertice import Vertice
from grafo.grafo import Grafo
from extras.settings import *
from .veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, pos:int, funcionarios:int):
        super().__init__(pos)
        self.funcionarios = funcionarios
        self.estado = 'indo'            # Atualizar pra nao quebrar, pq o código não aceita caminhao 'parado'

        self.qtdCompressao = 0
    
    def cheio(self):
        return self.qtdCompressao == MAX_CAMINHAO_COMPRESSAO

    def coletar(self, g:Grafo):
        v = g.vertices[self.caminho[0]]
        tempo = 0
        while self.caminho[0] in g.verticesCheios and not self.cheio():
            qtd = MAX_CAMINHAO_CARGA - self.carga
            
            if qtd >= v.lixo:               # Se a capacidade do caminhão for maior que o vértice
                lixo = v.lixo            
                v.lixo = 0                  # Esvazia totalmente e retorna a quantidade de lixo que tinha no vértice
                if v.n in g.verticesCheios:
                    g.verticesCheios.remove(v.n)
                self.carga += lixo
                self.comprimir()
                tempo += lixo//self.funcionarios
                continue
            
            v.lixo -= qtd                   # Senão subtrai por qtd e retorna esse qtd
            self.carga += qtd
            self.comprimir()
            tempo += qtd//self.funcionarios
        return tempo

    
    def __str__(self):
        return f"lixo: {self.carga}\ncaminho: {self.caminho}\nestado: {self.estado}\ncompressões: {self.qtdCompressao}"
    
    def comprimir(self):
        if self.carga == MAX_CAMINHAO_CARGA and self.qtdCompressao < MAX_CAMINHAO_COMPRESSAO:
            self.qtdCompressao += 1
            self.carga = self.carga*self.qtdCompressao//3
            

    def esvaziarCaminhao(self):
        self.carga = 0
        self.qtdCompressao = 0
        self.estado = "indo"
