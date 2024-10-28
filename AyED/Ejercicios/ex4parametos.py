def mensaje(sape):
    print("""---""")
    print(sape)
    print("""---""")

def elevar():
    x = int(input("Ingrese valor a elevar al cuadrado: "))
    y = pow(x,2)
    print(f"El resultado es: {y}")

mensaje("Este programa eleva al cuadrado.")
elevar()
