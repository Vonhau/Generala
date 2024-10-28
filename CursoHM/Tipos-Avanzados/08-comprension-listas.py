usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#    nombres.append(usuario[0])
# print(nombres)

# map
# nombresM = [usuario[0] for usuario in usuarios]
# print(nombresM)

# filter
# nombresF = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombresF)

# Lista filtrada y transformada
# nombresMF = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombresMF)

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
