for numero in range(5):
    print(numero, numero * "Hola Mundo")

buscar = 10
for numero in range(11):  # Iterables
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontrado")

for pito in "Ultimate Python":
    print(pito)
