"""
Realizar un programa que pida al usuario ingresar el nombre de un
empleado, los años de antigüedad, el sueldo y el área de trabajo. 
Por ejemplo: [ “Juan Pérez”, 14, 890000, “Contabilidad] El programa
deberá mostrar el nuevo sueldo del empleado incrementado en un 15%.
"""


def ingresar_datos():
    nombre = input("Ingrese el nombre del empleado: ")
    años_antiguedad = int(input("Ingrese la antiguedad del empleado: "))
    sueldo = float(input("Ingrese el sueldo: $"))
    nuevo_sueldo = sueldo * 1.15
    area_de_trabajo = input("Ingrese su área de trabajo: ")
    lista = [nombre, años_antiguedad, nuevo_sueldo, area_de_trabajo]
    print(lista)


ingresar_datos()
