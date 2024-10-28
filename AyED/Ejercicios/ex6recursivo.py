def suma_n_primeros(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + suma_n_primeros(n - 1)


n = int(input("Ingrese el valor de N: "))
resultado = suma_n_primeros(n)
print(f"La suma de los primeros {n} numeros es: {resultado}")
