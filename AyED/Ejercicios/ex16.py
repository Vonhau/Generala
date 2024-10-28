"""Implementar un polinomio utilizando POO"""


class Polinomio():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluar(self, x):
        return self.a * x**2 + self.b * x + self.c


polinomio1 = Polinomio(2, 3, 1)
x = 5
print(f"El resultado es: {polinomio1.evaluar(x)}")
