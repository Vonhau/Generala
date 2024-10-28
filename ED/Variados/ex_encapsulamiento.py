"""
Hola! Mi codigo realiza esta funcion general: bla bla
"""


class Coche():
    """
    Esta clase es un TAD de un auto.
    """

    def __init__(self, marca, modelo, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__vmax = velocidad_maxima

    def obtener_marca(self):
        return f"Marca: {self.__marca}"

    def obtener_modelo(self):
        return f"Modelo: {self.__modelo}"

    def obtener_velocidad(self):
        return f"Velocidad Máxima: {self.__vmax} km/h"

    def establecer_marca(self, marca):
        self.__marca = marca

    def establecer_modelo(self, modelo):
        self.__modelo = modelo

    def establecer_velocidad(self):
        try:
            vmax = int(
                input("Introduce la velocidad máxima del vehículo (mayor a 0): "))
            if vmax <= 0:
                raise ValueError("La velocidad debe ser superior a 0.")

            self.__vmax = vmax
            print(f"Velocidad máxima establecida en: {self.__vmax} km/h")

        except ValueError as ve:
            print(f"Error: {ve} Inténtalo de nuevo.")
            self.establecer_velocidad()


def main():
    """
    Esta funcion es la principal.
    """
    # GETS #
    coche1 = Coche("Toyota", "Ventus", 180)
    print(coche1.obtener_marca())
    print(coche1.obtener_modelo())
    print(coche1.obtener_velocidad())
    # SETS #
    coche1.establecer_marca("Ford")
    coche1.establecer_modelo("GT 2017")
    coche1.establecer_velocidad()


if __name__ == "__main__":
    main()
