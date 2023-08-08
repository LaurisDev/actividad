class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

Trebol = "Trebol"
Diamante = "Diamantes"
Corazon = "Crazones"
Pica = "Picas"



if __name__ == "__main__":
    carta_1 = Carta("10", Diamante)

print("El valor de su carta es de: ", carta_1.valor,"y la pinta de su carta es: ", carta_1.pinta)
