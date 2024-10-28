# Usamos PARAMETROS. Igualar un PARAMETRO a un valor es darle un valor por defecto.
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    # Esto es un parametro de la función
    print(f"bienvenido {nombre}, {apellido}")


hola("Joaquin", "Teixido")  # Le damos ARGUMENTOS
hola("Chanchito")

# Argumentos nombrados

hola(apellido="Teixido", nombre="Joaquin")
