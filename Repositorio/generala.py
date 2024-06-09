import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_total = 0
        self.puntajes_por_ronda = []
        self.resultados_tiradas = []
        self.dados_elegidos = []
        self.dados_sig_tirada = []

    def opciones(self, tirada):
        for dado in tirada:
            while True:
                respuesta = input(f"¿Desea guardar el dado {dado}? Y / N: ")
                if respuesta.lower() == 'y':
                    self.dados_elegidos.append(dado)
                    break
                elif respuesta.lower() == 'n':
                    self.dados_sig_tirada.append(dado)
                    break
                else:
                    print("Respuesta no válida. Por favor, responda con 'Y' / 'N'.")
        print(f"Los dados que elegiste son: {self.dados_elegidos}")
        print(f"Los dados que te quedan: {self.dados_sig_tirada}")


class Dado:

    def tirar_dado(self, cantidad=5):
        tirada = [random.randint(1, 6) for _ in range(cantidad)]
        tirada.sort()
        return tirada
# Este codigo se encarga de pedir al usuario que indique cuantos jugadores van a ser.


def ingresar_nombres_jugadores():
    """
    Esta función te pide la cantidad de jugadores,
    al igual que sus nombres. Te deberia devolver
    (por detrás) una lista con los jugadores.
    """
    jugadores = []

    while True:
        try:
            cant_jugadores = int(
                input("Por favor, ingrese el número de jugadores (2 - 4): "))
            if cant_jugadores < 2 or cant_jugadores > 4:
                print("Se ingresó un número inválido de jugadores, vuelva a intentarlo.")
            else:
                break
        except ValueError:
            print("Error, ingresó un texto o un número no válido. Vuelva a intentarlo.")

    # Bucle para conseguir los nombres y guardarlos en una lista que utiliza la clase Jugador.
    for _ in range(cant_jugadores):
        nombre = input(f"Por favor, ingrese el nombre del jugador {_ + 1}: ")
        jugador = Jugador(nombre)
        jugadores.append(jugador)

    return jugadores


def definir_orden_jugadores(jugadores):
    """
    Esta función utiliza los jugadores y define
    el orden en el que van a tirar según un
    número aleatorio (dado), deberia devolver
    el jugador con número más alto.
    """
    orden_dados = {jugador: random.randint(1, 6) for jugador in jugadores}
    orden_jugadores = sorted(
        orden_dados.items(), key=lambda x: x[1], reverse=True)
    return [jugador[0] for jugador in orden_jugadores]


def main():
    print("Bienvenido al juego de la Generala.")
    nombres_jugadores = ingresar_nombres_jugadores()
    orden_jugadores = definir_orden_jugadores(nombres_jugadores)

    print(f"Bien, para definir los turnos vamos a tirar {
          len(nombres_jugadores)} dados.")
    print("El orden se va a definir por los valores de los dados de mayor a menor.")
    print("El orden es el siguiente:")
    for i, jugador in enumerate(orden_jugadores):
        print(f"{i + 1}. {jugador.nombre}")

    print(f"¡¡Felicitaciones!! Empieza a jugar {orden_jugadores[0].nombre}")

    dados = Dado()
    tirada = dados.tirar_dado()
    print(f"{orden_jugadores[0].nombre} tira y le salen los dados: {tirada}")
    orden_jugadores[0].opciones(tirada)


if __name__ == "__main__":
    main()
# Este if permite que cuando llamo al codigo desde un import
# no se ejecute.
