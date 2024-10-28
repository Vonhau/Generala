numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])  # Recibe cualquier iterable, transforma a tupla.
print(punto)

# Las tuplas no se pueden modificar.

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito"
print(listaNumeros)
