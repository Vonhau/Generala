from tkinter import *


def mensaje():
    print("Mensaje del boton")


ventana = Tk()  # Crear la ventana donde van los widgets.
ventana.title("Calculadora (PROYECTO)")
ventana.resizable(0, 0)  # Width, Height, no deja redimensionar.
ventana.config(bg='#434750')
ventana.geometry("500x300")

lbl = Label(ventana, text="Este es un Label tkinter.")
lbl.pack()  # Ubicamos widgets en una posicion a traves de atributos.

btn = Button(ventana,
             text="Presione este boton para mensaje.",
             command=mensaje)

# btn.config(bg="#FCF5EA",
#           fg="#0B0B0B",)

btn["fg"] = "red"
btn["bg"] = "yellow"
btn.pack()

ventana.mainloop()  # Se monitorea la interaccion del usuario.

# Cambiar la extension a .pyw para que NO se ejecute la consola.
