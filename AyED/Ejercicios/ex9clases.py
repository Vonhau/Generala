# Implementaremos una clase llamada Persona que tendra como atributo (variable) 
# su nombre y dos metodos (funciones), uno de dichos metodos inicializara el atributo 
# nombre y el siguiente metodo mostrara en la pantalla el contenido del mismo.

class persona:
    def inicializar(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print(f"El nombre es: {self.nombre}")

# Main

persona1 = persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2 = persona()
persona2.inicializar("Santutu")
persona2.imprimir()