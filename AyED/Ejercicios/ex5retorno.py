def lista(bucle):
    enteros = []
    for i in range(bucle):
        x = int(input("Ingrese un entero: "))
        enteros.append(x)
    return enteros

bucle = int(input("Ingrese la cantidad de elementos que desea cargar en la lista: "))
print(f"Tu lista es: {lista(bucle)}")
