def numero_en_lista(lista, numero):
    if not lista:
        return f"{numero} no se encontró..."
    if lista[0] == numero:
        return f"{numero} está en la lista!"
    # Ese 1: significa que excluimos el primer elemento
    return numero_en_lista(lista[1:], numero)


# Ejemplo de uso RECURSIVO.
lista = [1, 2, 3, 4, 5]
print(numero_en_lista(lista, 3))  # True
print(numero_en_lista(lista, 7))  # False
