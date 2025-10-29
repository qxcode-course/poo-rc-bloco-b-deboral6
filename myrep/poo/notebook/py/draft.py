class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCarga(self) -> int:
        return self.__carga

    def getCapacidade(self) -> int:
        return self.__capacidade

    def setCarga(self, valor: int):
        if valor < 0:
            self.__carga = 0
        elif valor > self.__capacidade:
            self.__carga = self.__capacidade
        else:
            self.__carga = valor

    def gastar(self, tempo: int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0

    def carregar(self, tempo: int, potencia: int):
        self.__carga += tempo * potencia
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def getPotencia(self) -> int:
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def isLigado(self) -> bool:
        return self.__ligado

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria
        print("bateria instalada")

    def rmBateria(self) -> Bateria | None:
        b = self.__bateria
        self.__bateria = None
        print("bateria removida")
        return b

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador
        print("carregador conectado")

    def rmCarregador(self):
        self.__carregador = None
        print("carregador removido")

    def ligar(self):
        if self.__ligado:
            print("o notebook já está ligado")
            return

        if self.__bateria and self.__bateria.getCarga() > 0:
            self.__ligado = True
            print("notebook ligado")
        elif self.__carregador:
            self.__ligado = True
            print("notebook ligado usando carregador")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else:
            print("o notebook já está desligado")

    def usar(self, tempo: int):
        if not self.__ligado:
            print("erro: ligue o notebook primeiro")
            return

        print(f"usando por {tempo} minutos")

        if self.__bateria and not self.__carregador:
            if self.__bateria.getCarga() >= tempo:
                self.__bateria.gastar(tempo)
            else:
                usado = self.__bateria.getCarga()
                self.__bateria.gastar(usado)
                print(f"Notebook utilizado por {usado} minutos, bateria acabou")
                self.desligar()

        if self.__bateria and self.__carregador:
            potencia = self.__carregador.getPotencia()
            self.__bateria.carregar(tempo, potencia)
            print(f"Bateria carregando enquanto usa: ({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})")

        if not self.__bateria and self.__carregador:
            print("Notebook funcionando apenas no carregador")

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        print(f"Status: {status}", end=", ")
        if self.__bateria:
            print(f"Bateria: ({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})", end=", ")
        else:
            print("Bateria: Nenhuma", end=", ")
        if self.__carregador:
            print(f"Carregador: (Potência {self.__carregador.getPotencia()})")
        else:
            print("Carregador: Desconectado")

