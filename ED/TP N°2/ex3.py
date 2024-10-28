# Dada una secuencia de caracteres,
# obtener dicha secuencia invertida.

def invertir(cadena):
    # Hago lo mismo que en el ejercicio 2, solo que como es un string
    # no necesito hacer el paso extra de conversión.
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


# Programa
invertida = print(invertir("Tito"))
