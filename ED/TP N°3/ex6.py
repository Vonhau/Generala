"""
Ejercicio 6: Definir la clase Rectangulo. Un rectangulo pude ser 
definido de varias maneras, por ejemplo:
4 puntos: las 4 esquinas (sirve para cualquier poligono).
2 puntos: Idem anterior, pero usamos dos.
1 punto de referencia, base y altura.
(Elejir solo una e implementarla)
La clase debe contener los siguientes métodos:
Calcular el perimetro del rectangulo.
Clacular el area del rectangulo.
Chequear si el rectangulo es un cuadradro.
"""


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.x1, self.y1 = punto1
        self.x2, self.y2 = punto2
        # ABS devuelve el valor absoluto de la cuenta que hacemos.
        # En el ejemplo, da -2 y se devuelve su valor absoluto (positivo).
        self.base = abs(self.x2 - self.x1)
        self.altura = abs(self.y2 - self.y1)

    def perimetro(self):
        return 2*(self.base + self.altura)

    def area(self):
        return self.base * self.altura

    def chequeo_cuadrado(self):
        if self.base == self.altura:
            return "Es cuadrado."
        return "No es cuadrado"

    def __str__(self):
        return f"Base: {self.base}, Altura: {self.altura}"


def main():
    rectangulo = Rectangulo([2, 4], [4, 2])
    print(rectangulo)
    print(f"Tu perimetro es: {rectangulo.perimetro()}")
    print(f"Tu área es: {rectangulo.area()}")
    print(rectangulo.chequeo_cuadrado())


if __name__ == "__main__":
    main()
