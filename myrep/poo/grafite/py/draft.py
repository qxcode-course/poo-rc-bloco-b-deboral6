class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness.strip()
        self.size = size

    def usagePerSheet(self) -> int:
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
        else:
            raise ValueError(f"hardness inválida: {self.hardness}")

    def __str__(self):
        return f"{self.thickness:.1f}:{self.hardness}:{self.size}"

class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.grafite = None

    def insert(self, grafite: Grafite):
        if self.grafite is not None:
            print("fail: ja existe grafite")
            return
        if grafite.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.grafite = grafite

    def remove(self):
        if self.grafite is None:
            print("fail: nao existe grafite")
            return
        self.grafite = None

    def writePage(self):
        if self.grafite is None:
            print("fail: nao existe grafite")
            return

        if self.grafite.size <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.grafite.usagePerSheet()

        if self.grafite.size - gasto < 10:
            print("fail: folha incompleta")
            self.grafite.size = 10
            return

        self.grafite.size -= gasto

    def __str__(self):
        grafite_str = "null" if self.grafite is None else f"[{self.grafite}]"
        return f"calibre: {self.thickness:.1f}, grafite: {grafite_str}"


def main():
    pencil = None
    while True:
        line = input()
        args = line.split()
        print(f"${' '.join(args)}")

        if args[0] == "end":
            break
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))
        elif args[0] == "show":
            if pencil is not None:
                print(pencil)
        elif args[0] == "insert":
            if pencil is None:
                print("fail: nao existe lapis")
                continue
            grafite = Grafite(float(args[1]), args[2], int(args[3]))
            pencil.insert(grafite)
        elif args[0] == "remove":
            if pencil is not None:
                pencil.remove()
        elif args[0] == "write":
            if pencil is not None:
                pencil.writePage()

main()
