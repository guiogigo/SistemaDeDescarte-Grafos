
class Caminhao:
    percorrido = 0;
    tempoGasto = 0;
    qtdLixo = 0;
    
    def __init__ (self):
        self.tamanho = 100 # Caminhão irá comportar 100 cm3 de lixo 
        self.qtdCompressao = 0 # Quantidade de vezes que o lixo foi comprimido       

    def comprimir(self):
        if(self.qtdLixo == self.tamanho & self.qtdCompressao < 3):
            self.qtdLixo = self.qtdLixo/3
            self.qtdCompressao += 1;

    def recolherLixo(self, qtd: int):
        assert qtd >= 0

        self.qtdLixo += qtd

    def esvaziarCaminhao(self):
        self.qtdLixo = 0
        self.qtdCompressao = 0

