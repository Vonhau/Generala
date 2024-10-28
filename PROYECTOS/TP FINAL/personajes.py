class Personaje:
    """
    Esta es la clase generica o padre.
    De acá salen las subclases.
    """
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.habilidades = []
        self.poder = 500
        self.vida = 100
        self.nivel = 1

    def entrenar(self, horas):
        """
        Entrenamiento del personaje en funcion de cuantas horas este entrenando
        """
        if horas <= 0:
            print(f"{self.nombre} no entrenó.")
            return
        if horas > 24:
            print("Intentó entrenar demasiado sin descanso...")
            poder_reducido = (self.poder - horas) * 5
            self.poder = poder_reducido
            print(f"{self.nombre} entreno mucho y perdio{poder_reducido}de poder. Su poder ahora es {self.poder}")
            return
        
        poder_aumentado = horas * 10
        self.poder += poder_aumentado
        print(f"{self.nombre} ha entrenado durante {horas} horas y su poder aumento a {self.poder}.")
    
    def adquirir_habilidad(self, habilidad):
        """
        Añade una nueva habilidad a la lista de habilidades del personaje
        """
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} ha aprendido una nueva habilidad: ¡{habilidad}!")
        else:
            print(f"{self.nombre} ya tiene la habilidad: {habilidad}")
        
    def subir_nivel(self):
        """
        Sube de nivel al personaje, aumentando su poder base.
        """
        self.nivel += 1
        self.poder += self.nivel * 25 #aumenta el poder proporcional al nivel
        print(f"{self.nombre} ha subido al nivel {self.nivel}, poder actual: {self.poder}.")

    def __str__(self):
        return f"Nombre: {self.nombre}.\nNivel de Pelea: {self.poder}.\nRaza: {self.raza}.\nHabilidades: {self.habilidades}.\nNivel: {self.nivel}."


class Saiyajin(Personaje):
    """
    Esta es una subclase que hereda de la clase padre Personaje.
    En esta clase se deberia poder:
    - Transformarse.
    - ...
    """
    def __init__(self, nombre):
        # Coloco la raza como un string debido a que al heredar la clase Personaje esta lo pide como atributo obligatorio.
        # Queda pendiente ver si mantener o no el atributo raza de la clase Personaje.
        super().__init__(nombre, "Saiyajin") # Super es para heredar clases.
        self.nivel_transformacion = 0

    def transformarse(self):
        """ 
        Permite que un Saiyajin se transforme en el siguiente nivel de SSJ,
        multiplicando su poder de acuerdo al nivel alcanzado.
        """
        try:
            if self.nivel_transformacion >= 3:
                raise ValueError("¡Alcanzaste el nivel máximo de SSJ!")
            
            self.nivel_transformacion += 1
            multiplicador = self.nivel_transformacion + 1
            nuevo_poder = self.poder * multiplicador
            print(f"¡¡¡Su poder de {self.poder} ahora es {nuevo_poder}!!!")
            print(f"{self.nombre} se ha transformado en Super Saiyajin {self.nivel_transformacion}")
            self.poder = nuevo_poder
            
        except ValueError as e:
            print(f"Error, {e}")


class Namekuseijin(Personaje):
    """
    Esta es una subclase que hereda de la clase padre Personaje.
    En esta clase se deberia poder:
    - Transformarse.
    - ...
    """
    def __init__(self, nombre):
        super().__init__(nombre, "Namekuseijin")
        self.transformado = False

    def transformarse(self):
        """
        Cumple la misma función que su versión en el saiyajin, solo que es una transformación.
        """
        if self.transformado is False:
            print(f"¡{self.nombre} ha evolucionado a su forma Naranja!")
            nuevo_poder = self.poder * 5
            print(f"Su poder de {self.poder} ahora es {nuevo_poder}")
            self.poder = nuevo_poder
            self.transformado = True
            return 
        print(f"¡{self.nombre} ya se transformó!")

class Terrícola(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Terrícola") # Coloco la raza como un string.
        self.transformado = False
    
    #funcion que haga que el terricola entre en modo maestro y aumente su poder
    def usar_habilidad_especial(self):
        if not self.transformado: #para asegurar que solo pueda activar este habilidad una vez
            print(f"{self.nombre} ha activado su habilidad especial y entro en su modo")