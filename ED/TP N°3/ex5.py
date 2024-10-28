"""
Definir un TDA llamada fracción. Debe entenderse como fracción:
¾ . Como lo representaría?  Pensar los métodos definen el 
comportamiento de la fracción. 
"""
import math


class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador debe ser distinto de 0.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar_fraccion()  # Simplificamos automaticamente

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplificar_fraccion(self):
        # math.gcd es para encontrar el Máximo Común Divisor entre x e y.
        divisor_comun = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def sumar_fraccion(self, otra_fraccion):
        numerador_suma = (self.numerador * otra_fraccion.denominador) + \
            (otra_fraccion.numerador * self.denominador)
        denominador_suma = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador_suma, denominador_suma)

    def restar_fraccion(self, otra_fraccion):
        numerador_resta = (self.numerador * otra_fraccion.denominador) - \
            (otra_fraccion.numerador * self.denominador)
        denominador_resta = self.denominador * otra_fraccion.denominador
        return Fraccion(numerador_resta, denominador_resta)

    def multiplicar_fraccion(self, otra_fraccion):

        numerador_producto = self.numerador * otra_fraccion.numerador
        denominador_producto = self.denominador * otra_fraccion.denominador

        return Fraccion(numerador_producto, denominador_producto)

    def dividir_fraccion(self, otra_fraccion):

        # Multiplicar por el inverso de la segunda fracción
        numerador_resto = self.numerador * otra_fraccion.denominador
        denominador_resto = self.denominador * otra_fraccion.numerador

        return Fraccion(numerador_resto, denominador_resto)

# Programa principal #


def ingresar_fraccion():
    try:
        numerador = int(input("Ingrese el numerador: "))
        denominador = int(input("Ingrese el denominador: "))
        return Fraccion(numerador, denominador)
    except ValueError as e:
        print(f"Hubo un error: {e}. Por favor, intenta denuevo.")
        return ingresar_fraccion()  # Hacemos el bucle con una recursión.


def solicitar_fracciones():
    """Funcion auxiliar para pedir 2 fracciones.
        Ayuda a no repetir codigo en el menu."""
    fraccion1 = ingresar_fraccion()
    fraccion2 = ingresar_fraccion()
    return fraccion1, fraccion2


def menu():
    try:
        print("\n¡Bienvenido a la calculadora de fracciones! Elija una opción: ")
        print("1 - Sumar.\n2 - Restar.\n3 - Multiplicar.\n4 - Dividir.\n5 - Salir.")
        opcion = int(input("(1-5): "))

        # Comprobación de errores.

        if opcion < 1 or opcion > 5:
            raise ValueError("Debe ingresar un número entre 1 y 5.")

        if opcion == 1:
            fraccion1, fraccion2 = solicitar_fracciones()
            resultado = fraccion1.sumar_fraccion(fraccion2)
            print(f"Resultado de la suma: {resultado}")

        elif opcion == 2:
            fraccion1, fraccion2 = solicitar_fracciones()
            resultado = fraccion1.restar_fraccion(fraccion2)
            print(f"Resultado de la resta: {resultado}")

        elif opcion == 3:
            fraccion1, fraccion2 = solicitar_fracciones()
            resultado = fraccion1.multiplicar_fraccion(fraccion2)
            print(f"Resultado de la multiplicacion: {resultado}")

        elif opcion == 4:
            fraccion1, fraccion2 = solicitar_fracciones()
            resultado = fraccion1.dividir_fraccion(fraccion2)
            print(f"Resultado de la división: {resultado}")

        elif opcion == 5:
            print("¡Nos vemos!")
            return

        repetir = input("¿Deseas hacer otra operación? (Y/N): ").upper()
        if repetir == "N":
            print("¡Nos vemos!")
            return

        elif repetir != "Y":
            print("Opción no válida. ¡Nos vemos!")
            return
        else:
            menu()

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")
        # Llamada recursiva si ocurre un error
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
