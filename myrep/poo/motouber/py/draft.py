class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self._nome = nome
        self._dinheiro = dinheiro

    def get_nome(self):
        return self._nome

    def get_dinheiro(self):
        return self._dinheiro

    def adicionar_dinheiro(self, valor: float):
        self._dinheiro += valor

    def gastar_dinheiro(self, valor: float):
        if valor > self._dinheiro:
            valor_gasto = self._dinheiro
            self._dinheiro = 0
            return valor_gasto, False
        else:
            self._dinheiro -= valor
            return valor, True

    def __str__(self):
        return f"{self._nome}:{int(self._dinheiro)}"
    
class Moto:
    def __init__(self):
        self._custo = 0
        
        self._motorista = None
        self._passageiro = None
        
        print(f"Cost: {self._custo}, Driver: {Moto}, Passenger: {self._passageiro}")
    
def main():
    moto = Moto()
    while True:
        try:
            line = input().strip()
            if not line:
                continue

            if line.startswith("$"):
                line = line[1:]
                parts = line.split()
                cmd = parts[0]
                
                if cmd == "show":
                    print(moto)
            
        except EOFError:
            break
main()


