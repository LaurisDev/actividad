class Vehiculo:
    def __init__(self, velocidad_maxima: int, kilometraje: float):
        self.velocidad_maxima: int = velocidad_maxima
        self.kilometraje: float = kilometraje


if __name__ == "__main__":
    carro_1: Vehiculo = Vehiculo(600, 27.000)

print(carro_1.velocidad_maxima)
print(carro_1.kilometraje)