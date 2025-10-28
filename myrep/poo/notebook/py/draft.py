class Notebook:
    def __init__(self):
        self._ligado: bool = False
        self._bateria: Bateria
        
    def ligar(self):
        if not self._ligado:
            if self._bateria and self._bateria.getCarga() > 0:
               self._ligado  = True
               print("notebook ligado")
        
        else:
            print("o notebook ja esta ligado")

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print("notebook desligado")
        else: 
            print("o notebook ja esta desligado")

    def mostrar(self):
        if self._ligado:
            status = "ligado"
        else:
            status = "desligado"
        print(f"Status: {status}")

    def usar(self, valor: int):
        if self._ligado:
            self._bateria.setGastarCarga(valor)
            if self._bateria.getCarga() > 0:
                self._bateria.setCarga(0)
                self.desligar()

            print(f"usando por {valor} minutos")
        else:
            print("erro: ligue o notebook primeiro")

class Bateria:
    def __init__(self, capacidade: int):
        self._capacidade: int = capacidade
        self._carga: int = capacidade

    def getCarga(self) -> int:
        return self._carga
    def setCarga(self, valor: int):
        self._carga = valor
    
    def setGastarCarga(self, valor:int):
        self._carga -= valor

    def carrregar(self, capacidade: int, carga: int):
        if carga > capacidade:
            self._carga = capacidade
        else:
            self._carga = carga

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia
        




       
      