def Siracusa(k):
    if k == 1:
        print(f"El numero {k} ha llegado a un bucle, se detendrá la secuencia.")
        return 1
    elif k % 2 == 0:
        print(f"El numero {k} es par, se dividirá por dos.")
        return Siracusa(int(k/2))
    else:
        print(f"El numero {k} es impar, por ende se multiplicará por 3 y se le sumará 1")
        return Siracusa((k*3)+1)
    
k = int(input("Ingrese un número entero: "))
resultado = Siracusa(k)