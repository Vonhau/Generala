print("Bienvenido a la calculadora.")
print("Para salir escribe: salir")
print("Las operaciones son: suma, multi, div y resta.")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("Ingrese operación: ")
    if operacion.lower() == "salir":
        break
    n2 = input("Ingresa otro numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if operacion.lower() == "suma":
        resultado += n2
    elif operacion.lower() == "resta":
        resultado -= n2
    elif operacion.lower() == "multi":
        resultado *= n2
    elif operacion.lower() == "div":
        resultado /= n2
    else:
        print("No se ingresó una operación valida.")
        break

    print(f"El resultado de la operación {operacion} es: {resultado}")
