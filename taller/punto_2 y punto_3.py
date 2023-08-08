import random
import math

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self):
       self.x1 = random.randint(0, 10)
       self.y1 = random.randint(0, 10)

    def calcular_distancia(self, segundo_punto):
        distancia = math.sqrt((segundo_punto.x - self.x)**2 + (segundo_punto.y - self.y)**2)
        return distancia

if __name__ == "__main__":

    punto_1 = Punto(2, 5)
    punto_1.mostrar()
    punto_1.mover()
    punto_1.mostrar()

    punto_2 = Punto(4, 5)
    punto_2.mostrar()

    distancia_puntos = punto_1.calcular_distancia(punto_2)
    print("La distancia entre sus puntos es de:", distancia_puntos)
