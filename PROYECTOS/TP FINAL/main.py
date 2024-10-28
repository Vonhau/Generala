from personajes import *
from combate import *

def menu():
    print("¡Bienvenido al Dragon Ball Sparking 2D!")
    jugadores = []
    try:
        for _ in range(2):
            print(f"Introduzca los datos del personaje número {_ + 1}")
            nombre = input("Nombre: ")
            raza = int(input("Raza:\n1 - Saiyajin.\n2 - Namekuseijin.\n3 - Terricola.\n- "))
            if raza == 1:
                personaje = Saiyajin(nombre)
                jugadores.append(personaje)
            elif raza == 2:
                personaje = Namekuseijin(nombre)
                jugadores.append(personaje)
            elif raza == 3:
                personaje = Terrícola(nombre)
                jugadores.append(personaje)
            else:
                raise ValueError("Seleccione entre 1 y 3.")
            print("¡Personaje creado con éxito!")
            print("---")
            print(personaje) # Comprobacion de la creacion del personaje
            print("---")
    except ValueError as e:
        print(f"Error. {e}")

# A continuación, realizamos el ordenamiento de personajes segun su nivel de poder
# con arboles.

class Nodo: 
    def __init__(self, personaje):
        self.valor = personaje.nombre
        self.poder = personaje.poder
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
                self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

def main():
    menu()

if __name__ == "__main__":
    main()