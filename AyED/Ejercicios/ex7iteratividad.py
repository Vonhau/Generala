# implementar una funcion iterativa que retorne la suma de los primeros N numeros.

def suma(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Ingrese el valor de N: "))
resultado = suma(n)
print(f"La suma de los primeros {n} numeros es: {resultado}")