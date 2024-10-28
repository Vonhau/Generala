"""Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista"""


def carga(cantidad):
    lista = []
    for i in range(cantidad):
        num = int(input("Cargue un número: "))
        lista.append(num)
    return lista


def fija_cero(lista):
    for i in range(len(lista)):
        if lista[i] < 10:
            lista[i] = 0
    return lista


cantidad = int(input("¿Cuantos elementos desea cargar?: "))
lista = carga(cantidad)
print(f"La lista es {lista}")
lista_ceros = fija_cero(lista)
print(f"La lista con los números menores a 10 reemplazados por 0 es: {
      lista_ceros}")
