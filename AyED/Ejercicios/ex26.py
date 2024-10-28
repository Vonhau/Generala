class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if self.elementos:
            return self.elementos.pop()
        else:
            return None

    def peek(self):
        if self.elementos:
            return self.elementos[-1]
        else:
            return None

    def is_empty(self):
        return len(self.elementos) == 0


# Programa
pila = Pila()
print("LISTA VACIA")
print(pila.is_empty())
pila.push(1)
pila.push(2)
pila.push(3)
print("ULTIMO ELEMENTO")
print(pila.peek())
print("LISTA NO VACIA")
print(pila.is_empty())
print(pila.pop())
