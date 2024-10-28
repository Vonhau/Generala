# Ejercicio 2: Implementar una función que me permita ver si un
# número es capicua o no.

def numero_capicua(numero):
    # Para empezar, necesito convertir el numero en una cadena para poder compararlo.
    numero_str = str(numero)
    # Creo la cadena del numero invertido
    numero_invertido = ""
    for digito in numero_str:  # Recorro cada caracter de la cadena.
        # Invertimos la cadena acumulando los caracteres en orden inverso
        numero_invertido = digito + numero_invertido
    if numero_str == numero_invertido:
        print("Es capicua.")
    else:
        print("No es capicua")


# Programa
numero_capicua(55)
