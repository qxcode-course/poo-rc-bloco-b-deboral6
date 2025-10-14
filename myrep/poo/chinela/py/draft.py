class Chinela:
    def __init__(self):
        self.tam = 0
    
    def gettam(self):
        return self.tam 

    def settam(self,valor: int):
        if valor >= 20 and valor <= 50 and valor % 2 == 0:
            self.tam = valor
        elif valor % 2 != 0 or valor < 20:
            print("fail: você deve estar digitando um numero impar ou menor que 20")
         
chinela = Chinela()

while chinela.gettam() == 0:
    print("digite o tamanho da chinela")
    tam = int(input())

    chinela.settam(tam)

print("parabens voce comprou uma chinela tamanho:", chinela.gettam())    
