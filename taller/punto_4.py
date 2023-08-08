class Rectangulo:
    def __init__(self):
        self.punto_1 = (0, 3)
        self.punto_2 = (-6, 1)

    def calcular_perimetro(self):
        punto_x1, punto_y1 = self.punto_1
        punto_x2, punto_y2 = self.punto_2
        ancho = abs(punto_x2 - punto_x1)
        altura = abs(punto_y2 - punto_y1)
        perimetro = 2 * (ancho + altura)
        return perimetro

    def calcular_area(self):
        punto_x1, punto_y1 = self.punto_1
        punto_x2, punto_y2 = self.punto_2
        ancho = abs(punto_x2 - punto_x1)
        altura = abs(punto_y2 - punto_y1)
        area = (ancho * altura)
        return area

    def es_cuadrado(self):
        punto_x1, punto_y1 = self.punto_1
        punto_x2, punto_y2 = self.punto_2
        ancho = abs(punto_x2 - punto_x1)
        altura = abs(punto_y2 - punto_y1)
        if altura == ancho:
            return "Tu rectangulo es cuadrado"
        else:
            return "Tu rectangulo no es cuadrado"


if __name__ == "__main__":
    rectangulo = Rectangulo()
    print("PERIMETRO:", rectangulo.calcular_perimetro())
    print("AREA: ", rectangulo.calcular_area())
    print(rectangulo.es_cuadrado())



