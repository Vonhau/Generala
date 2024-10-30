class Habilidad:
    def __init__(self, nombre, personaje = None):
        self.nombre = nombre
        self.personaje = personaje
        self.mejoras = []

    def agregar_mejora(self, habilidad_mejorada):
        # permite agregar una mejora subhabilidad a lista
        # lo que hacemos aca es agregar la habilidad mejorada a lista self.mejoras
        self.mejoras.append(habilidad_mejorada)

    def mostrar_habilidades(self, nivel = 0):
        if self.personaje:
            personaje_info = f"{self.personaje}:"
        else:
            personaje_info = ""
        print(f"- {personaje_info}{self.nombre}")

        for mejora in self.mejoras:
            mejora.mostrar_habilidades(nivel + 1)


class ArbolHabilidades:
    def __init__(self, nombre_habilidad_raiz, personaje):
        # crea la habilidad raiz con el nombre del personaje
        self.raiz = Habilidad(nombre_habilidad_raiz, personaje)

    def buscar_habilidad(self, nodo, nombre_habilidad):
        # verificamos si el nombre del nodo actual es igual al nombre_habilidad
        if nodo.nombre == nombre_habilidad:
            return nodo

        # iteramos sobre cada hablidad en la lista mejoras, esto permite que descienda a los nodos hijos
        for mejora in nodo.mejoras:
            resultado = self.buscar_habilidad(mejora, nombre_habilidad)
            if resultado:
                return resultado
            print("No se ha encontrado dicha habilidad")

    def agregar_mejora(self, nombre_habilidad, nombre_mejora):
        # buscar la habilidad en el arbol y agregar una mejora
        habilidad = self.buscar_habilidad(self.raiz, nombre_habilidad)
        if habilidad:
            habilidad.agregar_mejora(Habilidad(nombre_mejora))
        else:
            print(f"Habilidad -{nombre_habilidad}- no encontrada")

    def mostrar_arbol(self):
        self.raiz.mostrar_habilidades()


# COLOCAR EN MAIN!!!
arbol = ArbolHabilidades("kamehameha", "Goku")
arbol.agregar_mejora("kamehameha", "kamehameha x10")
arbol.agregar_mejora("kamehameha x10", "kamehameha final")
arbol.agregar_mejora("kamehameha", "kamehameha x20")
arbol.agregar_mejora("kamehameha x20", "kamehameha Destructor")

arbol.mostrar_arbol()

