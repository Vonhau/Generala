# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
# si está regular (nota mayor o igual a 4).

class Alumno:
    def inicializar(self, nombre, calificacion):
        self.nombre = nombre
        self.nota = calificacion

    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de: {self.nota}")

    def regular(self):
        if self.nota >= 4:
            print("El alumno está aprobado.")
        else:
            print("El alumno esta desaprobado.")
    
alumno1 = Alumno()
alumno1.inicializar("Juan", 7)
alumno1.imprimir()
alumno1.regular()

alumno2 = Alumno()
alumno2.inicializar("Ana", 2)
alumno2.imprimir()
alumno2.regular()