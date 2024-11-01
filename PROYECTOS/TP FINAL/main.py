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
                personaje = Saiyajin(nombre, poder=500)
                jugadores.append(personaje)
            elif raza == 2:
                personaje = Namekuseijin(nombre, poder=500)
                jugadores.append(personaje)
            elif raza == 3:
                personaje = Terrícola(nombre, poder=500)
                jugadores.append(personaje)
            else:
                raise ValueError("Seleccione una raza entre 1 y 3.")
            print("¡Personaje creado con éxito!")
            print("---")
            print(personaje)  # Comprobación de la creación del personaje
            print("---")
    except ValueError as e:
        print(f"Error. {e}")


class Nodo:
    def __init__(self, personaje: Personaje):
        self.personaje = personaje
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, personaje: Personaje):
        """
        Si la raiz está vacía, se inserta el personaje como raíz.
        """
        if self.raiz is None:
            self.raiz = Nodo(personaje)
        else:
            self.insertar_recursivo(self.raiz, personaje)

    def insertar_recursivo(self, nodo, personaje):
        """
        Inserta el personaje de acuerdo con el poder.
        Si el poder del personaje a insertar es mayor al de la raíz, se inserta a la derecha
        y se corrobora si es mayor o menor, hasta llegar al último lugar.
        En caso de que el poder del personaje a insertar sea menor que el de la raíz, se inserta a la izquierda.
        """
        if personaje.poder < nodo.personaje.poder:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(personaje)
            else:
                self.insertar_recursivo(nodo.izquierda, personaje)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(personaje)
            else:
                self.insertar_recursivo(nodo.derecha, personaje)

    def buscar_maximo(self, nodo=None):
        """Busca el personaje con mayor nivel de poder."""
        if nodo is None:
            nodo = self.raiz
        # Continuamos a la derecha para encontrar el valor máximo
        while nodo.derecha is not None:
            nodo = nodo.derecha
        return nodo.personaje
    
    def imprimir_en_orden(self, raiz):
        if raiz is not None:
            self.imprimir_en_orden(raiz.izquierda)
            print(f"Nombre: {raiz.personaje.nombre}, Poder: {raiz.personaje.poder}")
            self.imprimir_en_orden(raiz.derecha)

def main():
    arbol = ArbolBinario()
    personajes = [
        Saiyajin("Goku", poder=9000),
        Namekuseijin("Piccolo", poder=8000),
        Terrícola("Krillin", poder=4000),
        Saiyajin("Vegeta", poder=8500),
        Terrícola("Yamcha", poder=3500)
    ]
    # Insertar personajes en el árbol binario
    for personaje in personajes:
        arbol.insertar(personaje)
    # Imprimir personajes en orden de poder del árbol
    print("\nPersonajes en orden de poder (Arbol Binario):")
    arbol.imprimir_en_orden(arbol.raiz)
    # Encontrar el personaje más fuerte en el árbol
    maximo = arbol.buscar_maximo()
    print(f"\n¡¡El personaje más fuerte es {maximo.nombre} con un poder de {maximo.poder}!!")

    print("\n---------")
    print("\nAhora, ordenamos en formato de cola y mostramos quien va a ser el siguiente en pelear según su nivel de pelea.")

    # Crear la cola de prioridad y agregar personajes
    cola_combate = ColadePrioridad()
    for personaje in personajes:
        cola_combate.agregar_personaje(personaje)

    print("\n---------")
    cola_combate.imprimir_cola()
    print("\n---------")

    # Mostrar el siguiente en combatir
    cola_combate.siguiente_combatiente()

    torneo = Torneo()
    for personaje in personajes:
        torneo.agregar_personaje(personaje)
    
    torneo.iniciar_torneo()

    
if __name__ == "__main__":
    main()
