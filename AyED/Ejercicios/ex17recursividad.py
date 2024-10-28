# Retornar el maximo de una lista.

def lista_nums(cantidad_numeros):
    lista = []
    for i in range(cantidad_numeros):
        numero_lista = int(input(f"Ingrese el {i + 1} número: "))
        lista.append(numero_lista)
    print(lista)
    return lista


def valor_maximo(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo


numeros_deseados = int(input("¿Cuantos numeros desea en su lista?: "))
listafinal = lista_nums(numeros_deseados)
v_maximo = valor_maximo(listafinal)
print(f"El valor máximo en la lista es: {v_maximo}")
