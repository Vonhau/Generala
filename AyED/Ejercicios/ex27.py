class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, elemento):
        self.elementos.append(elemento)

    def dequeue(self):
        if self.elementos:
            return self.elementos.pop(0)
        else:
            return None

    def peek(self):
        if self.elementos:
            return self.elementos[0]
        else:
            return None

    def is_empty(self):
        return len(self.elementos) == 0

    def get_elemento(self, indice):
        if 0 <= indice <= len(self.elementos):
            return self.elementos[indice]
        else:
            return None


# Programa
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(f"Uso de la funcion get_elemento: {cola.get_elemento(1)}")
print(cola.dequeue())
print(cola.dequeue())
print(cola.dequeue())
print(cola.dequeue())
print(cola.is_empty())
print(f"Uso de la funcion get_elemento: {cola.get_elemento(1)}")
