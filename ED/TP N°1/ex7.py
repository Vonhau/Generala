"""
Ejercicio 7: Escriba un programa que ingrese datos de patentes. El usuario deberá ingresar la
cantidad de datos a ingresar. Los datos de patente son: Nombre, Apellido, fecha de Inscripción,
patente.
"""

# Clase que representa a la Patente como un TAD, para su posterior registro.


class Patente:
    def __init__(self, nombre, apellido, fecha_inscripcion, numero_patente):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_inscripcion = fecha_inscripcion
        self.numero_patente = numero_patente

    def __str__(self):
        return f"Nombre: {self.nombre}.\nApellido: {self.apellido}.\nFecha de Inscripción: {self.fecha_inscripcion}.\nNúmero de Patente: {self.numero_patente}."


class RegistroPatentes:
    def __init__(self):
        self.patentes = []

    # Agregamos patente
    def agregar_patente(self, patente):
        self.patentes.append(patente)

    def buscar_patente(self, numero_patente):
        # Recorro cada patente en la lista.
        for patente in self.patentes:
            # Compruebo si la patente coincide.
            if patente.numero_patente == numero_patente:
                return patente
        # En caso que no se encuentre, retorna.
        print("No se encontró la patente")
        return

    def eliminar_patente(self, numero_patente):
        patente_a_eliminar = self.buscar_patente(numero_patente)
        if patente_a_eliminar is not None:
            self.patentes.remove(patente_a_eliminar)
            print("Patente removida con exito.")
            return
        print("No se encontró la patente")
        return

    def mostrar_patentes(self):
        if not self.patentes:
            print("No hay patentes registradas.")
        else:
            print("Listado de patentes registradas:")
            for patente in self.patentes:
                n = 1
                print(f"Patente N°{n}: \n{patente}")
                n += 1


# Ejercicio 8:
# Realizar un programa que imprima los apellidos de las personas que no pagarán el impuesto
# de patente. Tener en cuenta que los autos cuyas  patentes empiezan con R, S y T no pagan
# impuestos.

    def no_paga_impuesto(self):
        for patente in self.patentes:
            # Usamos IN para evitar ser repetitivos con varios OR.
            if patente.numero_patente[0] in ("R", "S", "T"):
                # En caso que el primer caracter sea R, S o T, imprimimos quien NO paga.
                print(f"{patente.apellido} no debe pagar el impuesto de patente.")


def ingresar_datos_patente():
    nombre = input("Ingrese el nombre del titular: ")
    apellido = input("Ingrese el apellido del titular: ")
    fecha_inscripcion = input("Ingrese la fecha de inscripción (DD/MM/AAAA): ")
    numero_patente = input("Ingrese el número de patente: ")
    # Instanciamos la patente
    return Patente(nombre, apellido, fecha_inscripcion, numero_patente)


def menu(registro):
    # Instancio el registro de las patentes.
    try:
        print("\n¡Bienvenido al menú de registro de patentes! Elija una opción: ")
        print("1 - Agregar patente.\n2 - Mostrar patentes.\n3 - Eliminar patentes.\n4 - Salir.")
        opcion = int(input("(1-4): "))

        # Comprobación de errores.

        if opcion < 1 or opcion > 4:
            raise ValueError("Debe ingresar un número entre 1 y 4.")

        if opcion == 1:
            cantidad = int(
                input("Ingrese la cantidad de patentes a registrar: "))
            for _ in range(cantidad):
                patente = ingresar_datos_patente()
                registro.agregar_patente(patente)

        elif opcion == 2:
            registro.mostrar_patentes()

        elif opcion == 3:
            numero_patente = input("Ingrese el numero de patente: ")
            registro.eliminar_patente(numero_patente)

        elif opcion == 4:
            print("¡Nos vemos!")
            return

        repetir = input("¿Deseas hacer otra operación? (Y/N): ")
        if repetir.upper() == "Y":
            menu(registro)

        if repetir.upper() == "N":
            print("¡Nos vemos!")
            return

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")
        # Llamada recursiva si ocurre un error
        menu(registro)


def main():
    registro = RegistroPatentes()
    menu(registro)
    registro.no_paga_impuesto()


# Programa principal
if __name__ == "__main__":
    main()
