def suma(*numeros):  # Es un ITERABLE
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 7, 7, 25)
