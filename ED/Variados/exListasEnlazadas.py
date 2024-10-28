# Implementa una lista enlazada doblemente enlazada (cada nodo tiene una
# referencia al siguiente y al anterior) y añade un método para eliminar un
# nodo específico.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista
        self.cola = None  # Fin de la lista

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza  # Apunta al antiguo primer nodo
            self.cabeza.anterior = nuevo_nodo  # El antiguo primer nodo apunta atrás
            self.cabeza = nuevo_nodo  # Actualiza la cabeza

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo  # El antiguo último nodo apunta al nuevo
            nuevo_nodo.anterior = self.cola  # El nuevo nodo apunta atrás
            self.cola = nuevo_nodo  # Actualiza la cola

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:  # Recorrer la lista
            if actual.valor == valor:
                if actual.anterior:  # No es el primer nodo
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:  # No es el último nodo
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:  # Es el primer nodo
                    self.cabeza = actual.siguiente
                if actual == self.cola:  # Es el último nodo
                    self.cola = actual.anterior
                return  # Nodo eliminado
            actual = actual.siguiente

    def recorrer(self):
        actual = self.cabeza
        while actual:  # Recorrer desde la cabeza hasta la cola
            print(actual.valor)
            actual = actual.siguiente

    def recorrer_inverso(self):
        actual = self.cola
        while actual:  # Recorrer desde la cola hasta la cabeza
            print(actual.valor)
            actual = actual.anterior


def main():
    lista = ListaDobleEnlazada()
    lista.agregar_al_inicio(5)
    lista.agregar_al_inicio(6)
    lista.agregar_al_inicio(7)
    lista.agregar_al_inicio(4)

    lista.agregar_al_final(10)
    lista.agregar_al_final(8)
    lista.agregar_al_final(9)
    lista.agregar_al_final(12)

    lista.recorrer()
    print("----")
    lista.recorrer_inverso()


if __name__ == "__main__":
    main()
