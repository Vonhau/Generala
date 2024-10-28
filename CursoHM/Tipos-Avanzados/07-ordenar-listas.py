numeros = [2, 4, 1, 25, 78, 22]

# Ordena la lista si no recibe argumento, ordena la lista al revés con reverse.
# numeros.sort(reverse=True)
# sorted crea una nueva lista ordenada. Lo mismo con reverse.
print(sorted(numeros, reverse=True))
print(numeros)

usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]


def ordena(elemento):
    # Hacemos que el sort tome el elemento 1 para que asi lo ordene.
    return elemento[1]


# Ponemos argumento posicional key para que pueda tomar la funcion ordena.
# Usar lambda nos ahorra escribir la función ordena.
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
