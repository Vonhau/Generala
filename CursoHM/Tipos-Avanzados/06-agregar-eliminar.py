mascotas = ["Wolfgang",
            "Pelusa",
            "Pulga",
            "Felipe",
            "Pulga",
            "Cosa"]

mascotas.insert(1, "Gatito")  # Añadimos un elemento a la lista donde queramos.
mascotas.append("Melvin")  # Añadimos un elemento al final.
# Elimina el primer elemento que se encuentra duplicado
mascotas.remove("Pulga")
# Elimina el elemento final si no ponemos nada o elimina el indice que le pongamos.
mascotas.pop(1)
del mascotas[0]
mascotas.clear()  # Vacia la lista
print(mascotas)
