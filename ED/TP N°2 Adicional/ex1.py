class Alumno():
    def __init__(self, legajo, nombre, apellido, contraseña):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.__contraseña = contraseña

    def __str__(self):
        return f"Número de Legajo: {self.legajo}.\nNombre: {self.nombre}.\nApellido: {self.apellido}.\nContraseña: {self.__contraseña}"


class Facultad():
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def imprimir_alumno(self):
        try:
            legajo = int(
                input("Introduce el numero de legajo del alumno que buscas: "))

            for alumno in self.alumnos:
                if alumno.legajo == legajo:
                    print(alumno)
                    return

            raise ValueError("No se encontró un alumno con ese legajo.")

        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
            # Llamada recursiva si ocurre un error
            self.imprimir_alumno()

    def legajo_menor(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return

        alumno_con_menor_legajo = min(
            self.alumnos, key=lambda alumno: alumno.legajo)
        return alumno_con_menor_legajo

    def nombre_mas_largo(self):
        if not self.alumnos:
            print("No hay alumnos registrados")
            return

        alumno_nombre_mas_largo = self.alumnos[0]
        for alumno in self.alumnos[1:]:  # Excluimos al primero en la lista
            if alumno.nombre < alumno_nombre_mas_largo:
                alumno_nombre_mas_largo = alumno
        return alumno_nombre_mas_largo

    def buscar_alumno(self):
        try:
            if not self.alumnos:
                raise ValueError("No hay alumnos registrados")

            legajo_ingresado = int(input(
                "Ingrese el legajo del alumno a controlar la clave: "))
            for alumno in self.alumnos:
                if alumno.legajo == legajo_ingresado:
                    return alumno
            raise ValueError("Alumno no encontrado.")

        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
            # Llamada recursiva si ocurre un error
            return self.buscar_alumno()

    def controlar_clave(self, alumno):
        try:
            alumno_encontrado = self.buscar_alumno()

            if len(alumno_encontrado._Alumno__contraseña) < 6:
                raise ValueError(
                    "La contraseña debe ser mayor a 6 caracteres")
            if not alumno_encontrado._Alumno__contraseña[-1].isdigit():
                raise ValueError("La contraseña debe terminar con un numero")

            print(f"La contraseña de {alumno_encontrado.nombre} es válida.")

        except ValueError as e:
            print(f"Error: {e}.")

    def verificar_claves(self):
        try:
            if not self.alumnos:
                raise ValueError("No hay alumnos registrados")

            for alumno in self.alumnos:
                self.controlar_clave(alumno)

        except ValueError as e:
            print(f"Error: {e}.")


def menu():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
