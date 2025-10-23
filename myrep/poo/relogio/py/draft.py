class Watch:
    def __init__(self, hora:int = 0, minuto: int = 0, segundo:int = 0):
        self.__hora: int = 0
        self.__minuto: int = 0
        self.__segundo: int = 0
        self.sethora(hora)
        self.setminuto(minuto)
        self.setsegundo(segundo)

    def sethora(self, valor: int):
        if valor >= 0 and valor <= 23:
            self.__hora = valor
        elif valor > 24:
            print("fail: hora invalida")
        else:
            print("fail: hora invalida")
        
    def setminuto(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.__minuto = valor
        else:
            print("fail: minuto invalido")

    def setsegundo(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.__segundo = valor
        else:
            print("fail: segundo invalido")
    
    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo == 60:
           self.__segundo = 0
           self.__minuto += 1
        if self.__minuto == 60:
           self.__minuto = 0
           self.__hora += 1
        if self.__hora == 24:
           self.__hora = 0

    def gethora(self):
        return self.__hora
    
    def getminuto(self):
        return self.__minuto
    
    def getsegundo(self):
        return self.__segundo
    
    def __str__(self) -> str:
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
        
def main():
    watch = Watch()
    while True:
        line: str = input()
        args: list[str] = line.split()
        print('$' + line)
        if len(args) == 0:
            continue
        elif args[0] == "end":
            break
        elif args[0] == "init":
            h, m, s = map(int, args[1:])
            watch = Watch(h,m,s)
        elif args[0] == "set":
            h, m, s = map(int, args[1:])
            watch.sethora(h)
            watch.setminuto(m)
            watch.setsegundo(s)
        elif args[0] == "show":
            print(watch)
        elif args[0] == "next":
            watch.nextSecond()
        else:
            print("fail: comando inválido")

main()