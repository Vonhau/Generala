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

    def eliminar_nodo(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual:
            if actual.valor == valor:
                anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def buscar_valor(self, valor):  # Busqueda Lineal
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False


# Programa
lista = ListaEnlazada()
lista.agregar_al_inicio(1)
lista.agregar_al_inicio(2)
lista.agregar_al_inicio(3)
lista.imprimir()
# Busco valor 3
print(lista.buscar_valor(3))
print(lista.buscar_valor(5))
lista.eliminar_nodo(2)
lista.imprimir()
# Lista nueva vacia, no muestra nada
lista2 = ListaEnlazada()
lista2.eliminar_nodo(2)
lista2.imprimir()
