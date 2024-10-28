"""
 Definir una función que reciba como parámetro una lista de números
 ( se sabe que la lista tiene 3 números, la función debe retornar la
 suma del 1er número y el último número de la Lista. Por ejemplo: 
 Lista= [ 4,3,8,9,2,11] La función deberá devolver 15.
"""


def suma_primero_ultimo(lista):
    suma = lista[0] + lista[-1]
    return suma


def main():
    lista = [4, 3, 8, 9, 2, 11]
    print(suma_primero_ultimo(lista))


main()
