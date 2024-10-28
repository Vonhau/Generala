# set = grupo o conjunto.
primer = {1, 1, 2, 2, 3, 4}  # Remueve los duplicados.
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo)  # Union de sets.
print(primer & segundo)  # Intersección
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # Diferencia simetrica

if 5 in segundo:
    print("Hola Mundo")
