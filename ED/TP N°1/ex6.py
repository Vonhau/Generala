class Producto:
    # Hago el producto como clase (TAD) para una mayor eficiencia.
    def __init__(self, codigo, nombre, marca, proveedor, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.proveedor = proveedor
        self.precio = precio
        self.stock = stock

    # Sobrecargo el método para que al mostrar el producto aparezcan sus datos.
    def __str__(self):
        return f"Código: #{self.codigo}.\nNombre: {self.nombre},\nMarca: {self.marca}.\nProveedor: {self.proveedor}.\nPrecio: ${self.precio}.\nStock: {self.stock} unidades."


class Kiosko:
    # Hago el kiosko como clase (TAD) para una mayor eficiencia.
    def __init__(self):
        self.productos = []

    def agregar_productos(self, producto):
        # Agrego el producto indicado a la lista con un append.
        self.productos.append(producto)

    def mostrar_productos(self):
        # Comprobacion si la lista esta vacia
        if not self.productos:
            print("No hay productos.")
        else:  # En caso que no:
            print("Productos del kiosko:")
            for producto in self.productos:
                n = 1  # Recorro cada elemento de la lista de productos.
                print(f"Producto {n}:\n {producto}")
                n += 1

    def buscar_producto(self, codigo):
        # Recorro cada producto en la lista.
        for producto in self.productos:
            # Compruebo si el codigo del producto es igual al codigo proporcionado.
            if producto.codigo == codigo:
                return producto
        # En caso que no se encuentre, retorna.
        return "No se encontró el producto."

    def eliminar_producto(self, codigo):
        # Creo una lista con el producto a eliminar y busco el producto.
        producto_a_eliminar = self.buscar_producto(codigo)
        if producto_a_eliminar:  # Si la lista tiene elementos, elimino con remove.
            self.productos.remove(producto_a_eliminar)
            print(f"Producto #{codigo} eliminado exitosamente.")
            return
        # Si esta vacia, aviso.
        return "No se encontró el producto."

# Menu para ingresar los datos


def ingresar_productos():
    codigo = int(
        input("Ingrese el código del producto (9999 = finalizar): "))
    if codigo == 9999:
        print("¡Nos vemos!")
        return

    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    proveedor = input("Ingrese el proveedor del producto: ")
    precio = float(input("Ingrese el precio del producto: $"))
    stock = int(input("Ingrese el stock del producto: "))

    return Producto(codigo, nombre, marca, proveedor, precio, stock)


# Menu para el kiosko
def menu(kiosko):
    try:
        print("\n¡Bienvenido al menú del kiosko! Elija una opción: ")
        print("1 - Agregar producto.\n2 - Mostrar productos.\n3 - Eliminar producto.\n4 - Salir.")
        opcion = int(input("(1-4): "))

        # Comprobación de errores.

        if opcion < 1 or opcion > 4:
            raise ValueError("Debe ingresar un número entre 1 y 4.")

        if opcion == 1:
            producto = ingresar_productos()
            # Comprobamos que la lista de producto de esté vacia.
            if producto is not None:
                # Agregamos al kiosko el producto.
                kiosko.agregar_productos(producto)
                print("Su producto fue correctamente ingresado.")

        elif opcion == 2:
            kiosko.mostrar_productos()

        elif opcion == 3:
            codigo = int(input("Ingrese el codigo del producto a eliminar: "))
            kiosko.eliminar_producto(codigo)

        elif opcion == 4:
            print("¡Nos vemos!")
            return

        repetir = input("¿Deseas hacer otra operación? (Y/N): ")
        if repetir.upper() == "Y":
            menu(kiosko)

        if repetir.upper() == "N":
            print("¡Nos vemos!")
            return

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")
        # Llamada recursiva si ocurre un error
        menu(kiosko)


def main():
    # Creamos la instancia del kiosko.
    kiosko = Kiosko()
    # Mostramos el menú.
    menu(kiosko)


# Programa principal
if __name__ == "__main__":
    main()
