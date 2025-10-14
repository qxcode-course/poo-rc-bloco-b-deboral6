class Camisa:
    def __init__(self):
        self.__tam: str = ""

    def gettam(self) -> str:
        return self.__tam 
    
    def settam(self, valor: str):
        tam_validos = ['PP', 'P', 'M', 'G', 'GG', 'XG']

        valor = valor.strip().upper()

        if valor in tam_validos:
            self.__tam = valor

            valor = valor.strip().upper()

        else:
            print("tamanho invalido")
            print("Os tamanhos validos são: " + " ".join(tam_validos))

roupa = Camisa()

while roupa.gettam() == "" :
    print("Digite seu tamanho de roupa (PP, P, M, G, GG, XG):")
    tam = input()
    roupa.settam(tam)

print("Parabens, você comprou uma roupa tamanho", roupa.gettam())







    