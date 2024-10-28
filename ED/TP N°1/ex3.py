def ingresar_lado(lado):
    try:
        valor = int(input(f"Ingresar el lado {lado}: "))
        if valor <= 0:
            raise ValueError(
                "El lado debe ser un número positivo mayor que cero")
        return valor
    except ValueError as e:
        print(f"Hubo un error: {e}. Por favor, intenta denuevo.")
        return ingresar_lado(lado)  # Hacemos el bucle con una recursión.


def calcular_perimetro():
    a = ingresar_lado("A")
    b = ingresar_lado("B")
    c = ingresar_lado("C")

    # Verifico si los lados forman un triangulo.
    if a + b > c and a + c > b and b + c > a:
        return f"El perímetro del triángulo es: {a + b + c}"
    else:
        return "Los lados ingresados no forman un triángulo."


def main():
    resultado = calcular_perimetro()
    if resultado:  # Comprueba que la variable tenga contenido distinto a None, False o vacio. En caso afirmativo imprime.
        print(resultado)


if __name__ == "__main__":
    main()
