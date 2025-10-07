class Chinela:
    def __init__(self):
        self.tam = 0
    
    def settam(self,valor: int):
        if tam >= 20 and tam tam <= 50 and tam % 2 == 0:
            self.tam += 2

chinela = Chinela()

while chinela.gettam() == 0:
    print("digite o tamanho da chinela")
    tam = int(input())

    chinela.settam(tam)

print("parabens voce comprou umma chinela tamanho:", chinela.gettam())    