#Confeccionar una clase que represente un empleado. 
# Definir como atributos su nombre y su sueldo. En el método init cargar
# los atributos por teclado y luego en otro método imprimir sus datos y por último uno 
# que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)

class Empleado():
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.sueldo = int(input("Ingrese el sueldo: $"))

    def imprimir(self):
        print(f"""---
El empleado de nombre {self.nombre} percibe un sueldo de: {self.sueldo}.""")
        
    def impuestos(self):
        print(f"""---
CALCULO DE IMPUESTOS
---""")
        if self.sueldo > 3000:
            print("El empleado debe pagar el impuesto a la ganancia.")
        else:
            print("El empleado no debe pagar el impuesto a la ganancia.")

empleado1 = Empleado()
empleado1.imprimir()
empleado1.impuestos()