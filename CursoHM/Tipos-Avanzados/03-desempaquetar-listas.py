# numeros = [1, 2, ]

# Feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Forma corta.
# primero, segundo, tercero = numeros

# ---

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Aca para almacenar todo el resto de valores que no queremos usamos el * como en las funciones.
primero, segundo, *otros, penu, ultimo = numeros
print(segundo, penu, otros)
