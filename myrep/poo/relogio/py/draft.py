class Watch:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def sethora(self, valor: int):
        if valor >= 0 and valor <= 23:
            self.hora = valor
        elif valor > 23:
            self.hora = 0

    def setminuto(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.minuto = valor
        elif valor == 60:
            self.sethora(1)

    def setsegundo(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.segundo = valor
        elif valor == 60:
            self.setminuto(1)

    def gethora(self):
        return self.hora
    
    def getminuto(self):
        return self.minuto
    
    def getsegundo(self):
        return self.segundo
    
    def __str__(self) -> str:
        return f"{self.hora:02d}: {self.minuto:02d}: {self.segundo:02d}"
        
def main():
    watch = Watch()
    while True:
        line = input()
        args = line.split(" ")
        if args [0] == "end":
            break
        elif args [0] == "show":
            print(watch)
        elif args [0] == "set":
            print()
        


    



    