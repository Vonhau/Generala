def elevar():
    x = int(input("Ingrese valor a elevar al cuadrado: "))
    y = pow(x,2)
    print(f"El resultado es: {y}")

def producto():
    print("A continuación ingrese dos valores a sacar su producto.")
    x = int(input("Ingrese primer valor: "))
    y = int(input("Ingrese segundo valor: "))
    print(f"El producto es: {x * y}")

elevar()
producto()
