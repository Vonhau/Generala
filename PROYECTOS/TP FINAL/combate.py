from personajes import *

class Combate:
    def __init__(self, personaje1: Personaje, personaje2: Personaje): # Anotacion de tipos, ayuda a que Pylint y el intérprete entiendan mejor.
        self.personaje1 = personaje1
        self.personaje2 = personaje2
         
    def iniciar_combate(self):
        print(f"el personaje {self.personaje1.nombre} inicio un combate con {self.personaje2.nombre} ")
        turno = 1 
        while self.personaje1.poder > 0 and self.personaje2.poder > 0:
            if turno % 2 != 0:
                self.atacar(self.personaje1, self.personaje2)
            else:
                self.atacar(self.personaje2, self.personaje1)
            turno += 1
        
        ganador = self.personaje1 if self.personaje1.poder > 0 else self.personaje2
        print(f"!{ganador.nombre} ha ganado el combate !")
        
    def atacar(self, atacante, defensor): 
        dano = atacante.poder // 2 # Calcula el daño basado en el poder del atacante
        defensor.poder -= dano  
        print(f"{atacante.nombre} ataca a {defensor.nombre} causando {dano} de daño. Poder restante de {defensor.nombre}: {defensor.poder}")
    
    def evolucion_poder(self, personaje1, personaje2):
        """funcion a revisar. se podria mejorar"""
        # Calcula el nuevo poder en función de si ganó o perdió el combate.
        def calcular_nuevo_poder(personaje, gano): 
            if isinstance(personaje, Saiyajin):
                return personaje.poder * 1.1 if gano else personaje.poder * 1.25
            if isinstance(personaje, (Namekuseijin, Terrícola)):
                return personaje.poder * 1.2 if gano else personaje.poder * 1.1
            return personaje.poder  #caso base si fuera otro tipo
        
        # Aplicar el aumento de poder para cada personaje
        personaje1_gano = personaje1.poder > 0
        personaje2_gano = personaje2.poder > 0
        
        personaje1.poder = calcular_nuevo_poder(personaje1, personaje1_gano)
        personaje2.poder = calcular_nuevo_poder(personaje2, personaje2_gano)
        
        print(f"El poder de {personaje1.nombre} después de la evolución es {personaje1.poder}.")
        print(f"El poder de {personaje2.nombre} después de la evolución es {personaje2.poder}.")