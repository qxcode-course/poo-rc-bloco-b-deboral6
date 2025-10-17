class Roupa:
    def __init__(self):
        self.__size: str = "" 

    def getsize(self):
        return self.__size
    
    def setsize(self, tam: str):
        tam = tam.strip().upper()
        tam_validos = ["PP", "P", "M", "G", "GG", "XG"]
        
        if tam in tam_validos:
            self.__size = tam
        else:
            print("fail: valor inválido tente: " + " ".join(tam_validos))


def main():
    roupa = Roupa()

    while True:
        try:
            rp = input().strip()
        except EOFError:
            break

        if rp == "$end":
            break

        elif rp == "$show":
            tam = roupa.getsize()
            print(f"size: ({tam})")

        elif rp.startswith("$size"):
            partes = rp.split()
            if len(partes) == 2:
                valor = partes[1]
                roupa.setsize(valor)
            else:
                print("fail: uso correto é $size <TAMANHO>")

        else:
            print("fail: comando inválido")

if __name__ == "__main__":
    main()







      






        
        

