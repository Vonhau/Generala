def presentacion():
    print("""Este programa carga dos valores por teclado,
          efectua la suma de ellos
          y muestra el resultado.""")

def carga():
    x = int(input("Ingrese primer valor a sumar: "))
    z = int(input("Ingrese segundo valor a sumar: "))
    print(f"El resultado es: {x + z}")

def despedida():
    print("¡¡Gracias por usar el programa!!")

presentacion()
carga()
despedida()
