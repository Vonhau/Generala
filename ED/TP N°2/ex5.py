# Desarrollar un algoritmo que permita calcular la siguiente serie:
# h(n) = 1 + 1/2 + 1/3 + ... + 1/n

def serie_armonica(numero):
    if numero == 1:  # Caso base
        return 1
    # En caso que sea distinto a cero, se llama a si misma con n - 1 y suma 1 / n.
    return 1 / numero + serie_armonica(numero - 1)


print(serie_armonica(5))
print(serie_armonica(1))
