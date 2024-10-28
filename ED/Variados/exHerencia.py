class InstrumentoMusical():
    def __init__(self, nombre, tipo, precio, material):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.material = material
        self.afinado = False  # Inicialmente, el instrumento no está afinado

    def afinar(self):
        self.afinado = True
        print(f"El instrumento {self.nombre} ha sido afinado.")


class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Strummm"


class Piano(InstrumentoMusical):
    def tocar(self):
        return "Ping Ping"


class Tambor(InstrumentoMusical):
    def tocar(self):
        return "Bong Bong"


def main():
    guitarra = Guitarra("Guitarra", "Cuerda", 500, "Madera")

    print(guitarra.tocar())  # Salida: La guitarra no está afinada.
    guitarra.afinar()
    print(guitarra.tocar())  # Salida: Sonido de guitarra: Strummm


if __name__ == "__main__":
    main()
