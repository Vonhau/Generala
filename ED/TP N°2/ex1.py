# Ejercicio 1: Definir una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.

def suma_aritmetica(numero):
    # Formula: S = n(n+1)/2
    suma = 0  # Inicializo la suma en 0 siguiendo la formula
    for i in range(numero + 1):  # Hago un bucle y por cada recorrido sumo uno.
        suma += i
    print(f"Tu resultado es: {suma}")
    return


def menu():
    try:
        numero = int(input(
            "Bienvenido a la calculadora de sucesiones.\nIngrese el número que quiere sumar: "))
        if numero < 0:
            raise ValueError("El número comprendido debe ser cero o positivo.")
        suma_aritmetica(numero)

        repetir = input("¿Deseas hacer otra operación? (Y/N): ")
        if repetir.upper() == "Y":
            menu()

        if repetir.upper() == "N":
            print("¡Nos vemos!")
            return

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")
        # Llamada recursiva si ocurre un error
        menu()


# Programa principal
if __name__ == "__main__":
    menu()
