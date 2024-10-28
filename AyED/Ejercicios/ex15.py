"""Desarrollar una clase que represente un punto en el plano y tenga 
los siguientes métodos: inicializar los valores de x e y que llegan como parámetros,
imprimir en que cuadrante se encuentra dicho punto (concepto matemático, 
primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)"""


class Plano():
    def __init__(self):
        self.x = int(input("X es: "))
        self.y = int(input("Y es: "))

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer Cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo Cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer Cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto Cuadrante")
        else:
            print("Punto de Origen")


plano1 = Plano()
plano1.cuadrante()
