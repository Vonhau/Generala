punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # Para acceder colocar la llave (string)
print(punto["y"])

punto["z"] = 45  # Agregar una nueva llave.
print(punto)
# Acceder a valores.
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
# Buscamos una llave que no existe y definimos su valor por defecto en caso de no encontrarla.
print(punto.get("lala", 97))

for valor in punto:
    # Accedemos a la llave en la primera. En la segunda accedemos al valor.
    print(valor, punto[valor])  # METODO menos eficaz

for valor in punto.items():  # Metodo mas eficaz
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])
