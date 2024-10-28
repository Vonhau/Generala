import math


class Punto():
    def __init__(self, puntoX, puntoY):
        self.puntoX = puntoX
        self.puntoY = puntoY

    def sumar_puntos(self, otro_punto):
        return Punto(self.puntoX + otro_punto.puntoX, self.puntoY + otro_punto.puntoY)

    def restar_puntos(self, otro_punto):
        return Punto(self.puntoX - otro_punto.puntoX, self.puntoY - otro_punto.puntoY)

    def modulo_punto(self):
        return math.sqrt(self.puntoX**2 + self.puntoY**2)

    def distancia_puntos(self, otro_punto):
        return math.sqrt((self.puntoX - otro_punto.puntoX)**2 + (self.puntoY - otro_punto.puntoY)**2)

    def get_punto(self):
        return f"Eje de Abscissas: {self.puntoX}, Eje de Ordenadas: {self.puntoY}"


# Principal
primerPunto = Punto(2, 3)
segundoPunto = Punto(7, 5)
print(f"Tu primer punto es: {primerPunto.get_punto()}")
print(f"Tu segundo punto es: {segundoPunto.get_punto()}")

# Calculos
suma = primerPunto.sumar_puntos(segundoPunto)
print(f"Suma entre los dos: {suma.get_punto()}")
resta = primerPunto.restar_puntos(segundoPunto)
print(f"Resta entre los dos: {resta.get_punto()}")

# Modulos
modulo1 = primerPunto.modulo_punto()
print(f"Modulo del punto 1: {modulo1}")
modulo2 = segundoPunto.modulo_punto()
print(f"Modulo del punto 2: {modulo2}")

# Distancia
distancia = primerPunto.distancia_puntos(segundoPunto)
print(f"Distancia entre los dos: {distancia}")
