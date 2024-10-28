# Plantear una clase Operaciones que solicite en el método init la carga de dos enteros e
# inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en
# otro método de la clase Operación y llamarlos desde el mismo método init.

class Operaciones():
    def __init__(self):
        self.int1 = int(input("Cargue el primer entero: "))
        self.int2 = int(input("Cargue el segundo entero: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        print(f"La suma de ambos enteros da: {self.int1 + self.int2}")

    def restar(self):
        print(f"La resta de ambos enteros da: {self.int1 - self.int2}")

    def multiplicar(self):
        print(f"La multiplicación de ambos enteros da:{self.int1 * self.int2}")

    def dividir(self):
        print(f"La división de ambos enteros da: {self.int1 / self.int2}")


Operaciones()
