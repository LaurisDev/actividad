import math


class Circulo:
    def __init__(self):
        self.centro: tuple[int, int] = (3, -2)
        self.radio: int = 5

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def calcular_pertenencia(self):
        punto_x, punto_y = punto
        centro_x, centro_y = self.centro
        pertenece = math.sqrt((punto_x - centro_x) ** 2 + (punto_y - centro_y) ** 2)
        if pertenece <= self.radio:
            return ("Su punto pertenece al circulo")
        else:
            return ("no pertenece")


if __name__ == "__main__":
    punto: tuple[int, int] = (6, -6)
    circulo = Circulo()
    print("AREA: ", circulo.calcular_area())
    print("PERIMETRO: ", circulo.calcular_perimetro())
    print(circulo.calcular_pertenencia())
