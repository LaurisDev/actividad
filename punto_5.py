import math


class Circulo:
    def __init__(self):
        self.radio = 5
        self.centro = (0, 2)

    def calcular_area(self):
        calcular = math.pi * self.radio ** 2
        return calcular


if __name__ == "__main__":
    area: Circulo = Circulo.calcular_area

print("El area de su circulo es de: ")