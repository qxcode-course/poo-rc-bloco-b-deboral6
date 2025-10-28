class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self._nome: str = nome
        self._dinheiro: int = dinheiro
    
    def __str__(self):
        return f"{self._nome}:{self._dinheiro}"
    
    def get_nome(self):
        return self._nome
    
    def get_dinheiro(self):
        return self._dinheiro
        
    def adicionar_dinheiro(self, valor: int):
        self._dinheiro += valor
    
    def gastar_dinheiro(self, valor: int):
        if valor > self._dinheiro:
            gasto = self._dinheiro
            self._dinheiro = 0
            return gasto, False
        else:
            self._dinheiro -= valor
            return valor, True 


class Moto:
    def __init__(self):
        self._custo: int = 0
        self._motorista: Pessoa | None = None
        self._passageiro: Pessoa | None = None
    
    def setDriver(self, nome: str, dinheiro: int):
        self._motorista = Pessoa(nome, dinheiro)
    
    def setPass(self, nome: str, dinheiro: int):
        self._passageiro = Pessoa(nome, dinheiro)
    
    def drive(self, km: int):
        if self._passageiro is None:
            print("fail: No passenger on the ride")
            return
        self._custo += km
    
    def leavePass(self):
        if self._passageiro is None:
            print("fail: No passenger to leave")
            return
        
        passageiro = self._passageiro
        motorista = self._motorista
        custo = self._custo

        pago, completo = passageiro.gastar_dinheiro(custo)
        motorista.adicionar_dinheiro(self._custo)

        if not completo:
            print("fail: Passenger does not have enough money")
        
        print(f"{passageiro.get_nome()}:{passageiro.get_dinheiro()} left")

        self._passageiro = None
        self._custo = 0

    def show(self):
        driver = str(self._motorista) if self._motorista else "None"
        passenger = str(self._passageiro) if self._passageiro else "None"
        print(f"Cost: {self._custo}, Driver: {driver}, Passenger: {passenger}")

def main():
    moto = Moto()
    while True:
        linha = input().strip()
        if not linha:
            continue

        comando = linha.split()
        cmd = comando[0]

        print(f"${' '.join(comando)}")
        if cmd in ("$end", "end"):
            break
        elif cmd == "show":
            moto.show()
        elif cmd == "setDriver":
            moto.setDriver(comando[1], int(comando[2]))
        elif cmd == "setPass":
            moto.setPass(comando[1], int(comando[2]))
        elif cmd == "drive":
            moto.drive(int(comando[1]))
        elif cmd == "leavePass":
            moto.leavePass()
        else:
            print("fail: invalid command")
main()