# Definir una función recursiva que imprime los números sucesivos
# desde n hasta 10. Por ejemplo funcion_sucesivo (6)
# Imprimirá: 6,7,8,9,10

def funcion_sucesivo(numero):
    while numero != 11:
        print(numero)
        numero = numero + 1


funcion_sucesivo(6)
funcion_sucesivo(2)
