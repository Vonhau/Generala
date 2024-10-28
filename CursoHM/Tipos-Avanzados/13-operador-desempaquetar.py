lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista)  # Operador desempaquetador

lista2 = [5, 6]

combinada = [*lista, *lista2]  # Combinamos ambas listas
print(combinada)

# Version para diccionarios
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
