animal = " chaNchito fElIz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("cH"))  # Indice (donde está)
print(animal.replace("Nch", "j"))  # Reemplaza
print("Nch" in animal)  # Pregunta SI se encuentra o no (True = Si, False = No)
# Pregunta si NO se encuentra (True = No, False = Si)
print("Nch" not in animal)
