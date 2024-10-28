def invertir(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida


def eliminar_espacios(cadena):
    nuevo_texto = ""
    for char in cadena:
        if char != " ":
            nuevo_texto += char  # Concatenamos caracteres
    return nuevo_texto


def es_palindromo(cadena):
    cadena = eliminar_espacios(cadena)
    cadena_invertida = invertir(cadena)
    if cadena.lower() == cadena_invertida.lower():
        print(f"{string} es un palindromo")
    else:
        print(f"{string} no es un palindromo")


string = str(input("Ingrese palabra: "))
es_palindromo(string)
