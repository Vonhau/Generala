from personajes import *
import heapq
import random
import time

class Combate:
    def __init__(self, personaje1: Personaje, personaje2: Personaje): # Anotacion de tipos, ayuda a que Pylint y el intérprete entiendan mejor.
        self.personaje1 = personaje1
        self.personaje2 = personaje2
         
    def iniciar_combate(self):
        print(f"\n⚔️ ¡El combate entre {self.personaje1.nombre} y {self.personaje2.nombre} comienza! ⚔️\n")
        turno = 1 
        while self.personaje1.poder > 0 and self.personaje2.poder > 0:
            if turno % 2 != 0:
                self.atacar(self.personaje1, self.personaje2)
            else:
                self.atacar(self.personaje2, self.personaje1)
            turno += 1
            time.sleep(1) # sirve para dar un intervalo de 1 segundo
        
        ganador = self.personaje1 if self.personaje1.poder > 0 else self.personaje2
        print(f"\n🎉 ¡{ganador.nombre} ha ganado el combate! 🎉\n")
        
    def atacar(self, atacante, defensor): 
        # Probabilidad de ataque crítico (15% de posibilidades)
        critico = random.random() < 0.15
        if critico:
            dano = atacante.poder // 1.5 # daño critico, aumenta el daño 
            mensaje_critico = random.choice([f"💥 ¡{atacante.nombre} realiza un ataque CRÍTICO devastador!",
                f"🔥 {atacante.nombre} ha desatado todo su poder con un golpe CRÍTICO!",
                f"⚡️ ¡Increíble! {atacante.nombre} golpea con un ataque CRÍTICO feroz!"
                ])
            print(mensaje_critico)
        else:
            dano = atacante.poder // 2 # daño normal
        
        #reducimos el poder del defensor
        defensor.poder -= dano

        #mensajes dinamicos de los ataques
        mensaje_ataque = random.choice([
            f"{atacante.nombre} lanza un ataque contra {defensor.nombre}, causando {dano} de daño.",
            f"¡{atacante.nombre} golpea fuertemente a {defensor.nombre}!",
            f"{atacante.nombre} ataca a {defensor.nombre}, infligiendo {dano} de daño."
        ])
        print(mensaje_ataque)

        # Mostrar el poder restante del defensor
        if defensor.poder > 0:
            print(f"⚡️ El poder restante de {defensor.nombre} es {defensor.poder:.2f}\n")
        else:
            print(f"❌ {defensor.nombre} ha sido derrotado.\n")

    def evolucion_poder(self, personaje1, personaje2):
        """funcion a revisar. se podria mejorar"""
        # Calcula el nuevo poder en función de si ganó o perdió el combate.
        def calcular_nuevo_poder(personaje, gano): 
            if isinstance(personaje, Saiyajin):
                nuevo_poder = personaje.poder * (1.25 if gano else 1.1)
            elif isinstance(personaje, (Namekuseijin, Terrícola)):
                nuevo_poder = personaje.poder * (1.2 if gano else 1.1)
            else:
                nuevo_poder = personaje.poder
            
            return max(0, nuevo_poder) # evitar poderes negativos
        
        ganador = personaje1 if personaje1.poder > 0 else personaje2
        perdedor = personaje2 if ganador == personaje1 else personaje1

        # Aplicar el aumento de poder para cada personaje
        ganador.poder = calcular_nuevo_poder(ganador,True)
        perdedor.poder = calcular_nuevo_poder(perdedor,False)
        
        print(f"El poder de {ganador.nombre} después de la evolución es {ganador.poder}.")
        print(f"El poder de {perdedor.nombre} después de la evolución es {perdedor.poder}.")

class ColadePrioridad:
    def __init__(self):
        self.heap = []
    
    def agregar_personaje(self, personaje: Personaje):
        # Insertamos el personaje en la heap, usando el nivel de poder con signo negativo
        heapq.heappush(self.heap, (-personaje.poder, personaje)) #utilizamos heappush para insertar el item en el heap
    
    def siguiente_combatiente(self):
        # extraemos el personaje con mayor prioridad (nivel de poder)
        if self.heap:
            return heapq.heappop(self.heap)[1] # utilizamos heappop para retornar el elemento mas pequeño
        else:
            print("no hay personajes en la cola.")
            return None

    def imprimir_cola(self):
        #imprimimos el estado de la cola
        print("\nCola de personajes ordenada por prioridad\n")
        for _, personaje in sorted(self.heap):
            print(f"Nombre: {personaje.nombre}, Poder: {personaje.poder}")

class Torneo:
    def __init__(self):
        self.cola_combate = ColadePrioridad()

    def agregar_personaje(self, personaje):
        self.cola_combate.agregar_personaje(personaje)
    
    def iniciar_torneo(self):
        print("! iniciando el torneo de combates!\n ")

        while len(self.cola_combate.heap) > 1:
            # Sacar los dos personajes con mayor prioridad de la cola
            personaje1 = self.cola_combate.siguiente_combatiente()

            # Verificar si hay otro personaje para combatir
            if len(self.cola_combate.heap) > 0:
                personaje2 = self.cola_combate.siguiente_combatiente()
            else:
                # Si no hay otro personaje, el torneo termina y este personaje es el ganador
                print(f"¡{personaje1.nombre} es el ganador del torneo con un poder de {personaje1.poder}!")
                return

            #creamos el combate
            combate = Combate(personaje1, personaje2)
            combate.iniciar_combate()

            #calculamos la evolucion de poder
            combate.evolucion_poder(personaje1, personaje2)

            # Después de la evolución, volver a agregar los personajes a la cola si todavía tienen poder
            if personaje1.poder > 0:
                self.cola_combate.agregar_personaje(personaje1)    
            if personaje1.poder > 0:
                self.cola_combate.agregar_personaje(personaje1)
        
        # Cuando solo queda un personaje en la cola
        if len(self.cola_combate.heap) == 1:
            ganador = self.cola_combate.siguiente_combatiente()
            print(f"¡El ganador final del torneo es {ganador.nombre} con un poder de {ganador.poder}!")