import random

class NodoArbol:
    def __init__(self, data):
        """
        Inicializa un nodo del árbol con un valor (data) y una lista vacía de hijos.
        """
        self.data = data
        self.hijos = []

    def agregar_hijo(self, hijo):
        """
        Agrega un nodo hijo a la lista de hijos del nodo actual.
        Evita agregar el mismo hijo más de una vez.
        """
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        else:
            print("El hijo ya está en la lista de hijos.")

    def obtener_data(self):
        """
        Retorna el valor (data) del nodo.
        """
        return self.data

    def obtener_hijos(self):
        """
        Retorna la lista de hijos del nodo.
        """
        return self.hijos

    def eliminar_hijo(self, hijo):
        """
        Elimina un nodo hijo de la lista de hijos si existe.
        """
        if hijo in self.hijos:
            self.hijos.remove(hijo)
        else:
            print("El hijo no existe en la lista de hijos.")

    def contar_hijos(self):
        """
        Devuelve el número de hijos directos del nodo.
        """
        return len(self.hijos)

    def buscar_nodo(self, valor):
        """
        Busca un nodo por su valor (data) en el árbol. Retorna el nodo si lo encuentra,
        de lo contrario retorna None.
        """
        if self.data == valor:
            return self
        for hijo in self.hijos:
            resultado = hijo.buscar_nodo(valor)
            if resultado:
                return resultado
        return None

    def contar_todos_los_nodos(self):
        """
        Cuenta el número total de nodos en el árbol (incluyendo el nodo actual y todos sus hijos).
        """
        total = 1  # Contar el nodo actual
        for hijo in self.hijos:
            total += hijo.contar_todos_los_nodos()
        return total

    def dibujar_arbol(self, nivel=0):
        """
        Genera una representación visual del árbol de forma jerárquica.
        """
        resultado = "  " * nivel + "└── " + str(self.data) + "\n"
        for hijo in self.hijos:
            resultado += hijo.dibujar_arbol(nivel + 1)
        return resultado

    def __str__(self):
        """
        Sobreescribe la representación en string del árbol para que al usar print en un nodo,
        se dibuje la estructura completa del árbol.
        """
        return self.dibujar_arbol()

# Ejemplo de uso de la clase NodoArbol
if __name__ == "__main__":
    # Crear el nodo raíz
    root = NodoArbol("raiz")

    # Crear nodos hijos
    child1 = NodoArbol("nodo 1")
    child2 = NodoArbol("nodo 2")
    child3 = NodoArbol("nodo 3")

    # Agregar hijos a la raíz
    root.agregar_hijo(child1)
    root.agregar_hijo(child2)
    root.agregar_hijo(child3)

    # Crear hijos adicionales para cada nodo hijo
    for i in range(1, random.randint(1, 4)):
        child = NodoArbol(f"nodo {i}")
        root.agregar_hijo(child)
        for j in range(1, random.randint(1, 4)):
            subchild = NodoArbol(f"nodo {i}.{j}")
            child.agregar_hijo(subchild)
            for k in range(1, random.randint(1, 3)):
                subsubchild = NodoArbol(f"nodo {subchild.obtener_data()}.{k}")
                subchild.agregar_hijo(subsubchild)

    # Imprimir la estructura del árbol
    print(root)

    # Buscar un nodo
    valor_buscado = "nodo 2"
    nodo_encontrado = root.buscar_nodo(valor_buscado)
    if nodo_encontrado:
        print(f"Nodo encontrado: {nodo_encontrado.data}")
    else:
        print(f"Nodo con valor '{valor_buscado}' no encontrado.")

    # Contar el número total de nodos
    total_nodos = root.contar_todos_los_nodos()
    print(f"El número total de nodos en el árbol es: {total_nodos}")

