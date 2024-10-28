class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def ordenar(self):
        if not self.cabeza or not self.cabeza.siguiente:
            return

        actual = self.cabeza
        while actual.siguiente:
            minimo = actual
            siguiente = actual.siguiente
            while siguiente:
                if siguiente.valor < minimo.valor:
                    minimo = siguiente
                siguiente = siguiente.siguiente
            actual.valor, minimo.valor = minimo.valor, actual.valor
            actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            # Imprime y deja un espacio entre cada valor que va a imprimir.
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print()


# Programa
lista = ListaEnlazada()
lista.agregar_al_inicio(5)
lista.agregar_al_inicio(9)
lista.agregar_al_inicio(2)
lista.agregar_al_inicio(8)
print("La lista original es: ")
lista.imprimir()
print("La lista ordenada es: ")
lista.ordenar()
lista.imprimir()
