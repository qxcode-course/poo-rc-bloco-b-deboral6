class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        
    def ligar(self):
        if not self.__ligado:
            self.__ligado  = True
            print("notebook ligado")
        else:
            print("o otebook ja esta ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else: 
            print("o notebook ja esta desligado")

    def mostrar(self):
        if self.__ligado:
            status = "ligado"
        else:
            status = "desligado"
        print(f"Status: {status}")

    def usar(self, valor: int):
        if self.__ligado:
            print(f"usando por {valor} minutos")
        else:
            print("erro: ligue o notebook primeiro")

class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade
        




       
      