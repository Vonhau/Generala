import math


def simplificar_fraccion(numerador, denominador):
    # math.gcd es para encontrar el Máximo Común Divisor entre x e y.
    divisor_comun = math.gcd(numerador, denominador)
    # devuelve el numerador dividido el mcd y el denominador dividido el mcd.
    return [numerador // divisor_comun, denominador // divisor_comun]


def sumar_fraccion(fraccion1, fraccion2):
    numerador1, denominador1 = fraccion1
    numerador2, denominador2 = fraccion2

    numerador_suma = numerador1 * denominador2 + numerador2 * denominador1
    denominador_suma = denominador1 * denominador2

    return simplificar_fraccion(numerador_suma, denominador_suma)


def restar_fraccion(fraccion1, fraccion2):
    numerador1, denominador1 = fraccion1
    numerador2, denominador2 = fraccion2

    numerador_resta = numerador1 * denominador2 - numerador2 * denominador1
    denominador_resta = denominador1 * denominador2

    return simplificar_fraccion(numerador_resta, denominador_resta)


def multiplicar_fraccion(fraccion1, fraccion2):
    numerador1, denominador1 = fraccion1
    numerador2, denominador2 = fraccion2

    numerador_producto = numerador1 * numerador2
    denominador_producto = denominador1 * denominador2

    return simplificar_fraccion(numerador_producto, denominador_producto)


def dividir_fraccion(fraccion1, fraccion2):
    numerador1, denominador1 = fraccion1
    numerador2, denominador2 = fraccion2

    # Multiplicar por el inverso de la segunda fracción
    numerador_division = numerador1 * denominador2
    denominador_division = denominador1 * numerador2

    return simplificar_fraccion(numerador_division, denominador_division)

# Programa principal #


def ingresar_fraccion():
    try:
        numerador = int(input("Ingrese el numerador: "))
        denominador = int(input("Ingrese el denominador: "))
        if denominador == 0:
            raise ValueError(
                "El denominador debe ser un entero distinto de 0")
        else:
            return [numerador, denominador]  # Devuelve la fraccion como lista.
    except ValueError as e:
        print(f"Hubo un error: {e}. Por favor, intenta denuevo.")
        return ingresar_fraccion()  # Hacemos el bucle con una recursión.


# Menú recursivo con manejo de excepciones
def mostrar_menu():
    try:
        print("\nBienvenido a la calculadora de fracciones, elija una operacion.")
        print("1: Sumar.\n2: Restar.\n3: Multiplicar.\n4: Dividir.\n5: Salir")

        opcion = int(
            input("(1-5): "))

        # Comprobación de errores y opcion de salir.
        if opcion < 1 or opcion > 5:
            raise ValueError("Debe ingresar un número entre 1 y 5.")
        if opcion == 5:
            print("¡Nos vemos!")
            return

        fraccion1 = ingresar_fraccion()
        fraccion2 = ingresar_fraccion()

        if opcion == 1:
            resultado = sumar_fraccion(fraccion1, fraccion2)
        elif opcion == 2:
            resultado = restar_fraccion(fraccion1, fraccion2)
        elif opcion == 3:
            resultado = multiplicar_fraccion(fraccion1, fraccion2)
        elif opcion == 4:
            resultado = dividir_fraccion(fraccion1, fraccion2)

        # Muestro la posicion 0 y 1 de la lista que me devuelve la operacion.
        input(f"Tu fracción es: {resultado[0]}/{resultado[1]}")
        repetir = input("¿Deseas hacer otra operación? (Y/N): ")
        if repetir == "Y":
            mostrar_menu()
        if repetir == "N":
            print("¡Nos vemos!")
            return
        # Llamada recursiva para mostrar el menú nuevamente

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")
        # Llamada recursiva si ocurre un error
        mostrar_menu()


# Programa principal
if __name__ == "__main__":
    mostrar_menu()
