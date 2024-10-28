"""
Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir
una función que muestre el número más alto, escriba el programa que
invoque a la función. 
"""


def num_mas_alto(lista):
    num = max(lista)
    print(f"El número más alto de la lista es: {num}")
    return


def main():
    lista = [1, 14, 56, 43, 23, 46, 58, 123, 67]
    num_mas_alto(lista)


if __name__ == "__main__":
    main()
