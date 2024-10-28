mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas[0:3])  # Muestra 3 elementos, contando desde 0 (0,1,2)
print(mascotas[2:])  # Muestra desde el indice 2 hasta el final del array
print(mascotas[-1])  # Muestra el ultimo elemento.
print(mascotas[::2])  # Toma un elemento, el sig lo salta.

numeros = list(range(21))
print(numeros[1::2])  # Impares
print(numeros[::2])  # Pares
