mascotas = ["Pelusa", "Wolfgang", "Pulga", "Felipe", "Wolfgang", "Cosa"]

# Cuenta cuantas veces se encuentra el elemento en la lista.
print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:
    # index comprueba si el elemento que buscamos está, si es True devuelve su indice, si es False tira error.
    print(mascotas.index("Wolfgang"))
