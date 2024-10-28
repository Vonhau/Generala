"""1.1-Crear una clase Comprador, que contenga los datos básicos de una persona: 
nombre, dirección, teléfono, fecha de nacimiento y un campo puntaje que dependerá de las compras que realice. 
En el constructor, se deben inicializar todos los campos, y por defecto, el valor de puntaje será 0 (cero). 
Implementar los métodos para sumar o restar puntos del puntaje del comprador."""


class Buyer:
    def __init__(self, name, address, phone, email, birth_date):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birth_date = birth_date
        self.score = 0

    def add_score(self, points):
        self.score += points

    def remove_score(self, points):
        if self.score - points < 0:
            raise ValueError("Error, no se puede tener un puntaje negativo.")
        self.score -= points

    def get_buyer(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}, Birth Date: {self.birth_date}"


"""1.2-Crear una clase Articulos que contenga los campos identificador (tipo entero positivo),
nombre, descripcion, marca, precio (float) y puntos. 
En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. 
IMPORTANTE: los puntos no pueden ser negativos."""


class Article():
    def __init__(self, identifier, name, description, mark, price, points):
        self.id = identifier
        self.name = name
        self.description = description
        self.mark = mark
        self.price = price
        self.points = points

    def set_id(self, new_id):
        self.id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_description(self, new_description):
        self.description = new_description

    def set_mark(self, new_mark):
        self.mark = new_mark

    def set_price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise ValueError("Error, coloca un numero.")
        self.price = new_price

    def set_points(self, new_points):
        if new_points < 0:
            raise ValueError("Error, los puntos no pueden ser negativos.")
        self.points = new_points

    def get_article(self):
        return self.id, self.name, self.description, self.price, self.points


def main():
    buyer1 = Buyer("Joako", "Avenida Falsa 123",
                   "123 123 123", "joateixido15@gmail.com", "11/06/2006")
    buyer1.add_score(20)
    buyer1.remove_score(20)
    print(buyer1.get_buyer())
    print(f"El puntaje de {buyer1.name} es: {buyer1.score}")

    article1 = Article(
        "01", "Remera", "Una prenda que se coloca en el tren superior.", "Jaguar", 15.66, 20)
    print(f"Articulo 1 original: {article1.get_article()}")

    article1.set_id("1")
    article1.set_name("Pantalon")
    article1.set_description("Una prenda que se coloca en el tren superior.")
    article1.set_mark("Converse")
    article1.set_price(16)
    article1.set_points(25)

    print(f"Articulo 1 modificado: {article1.get_article()}")


if __name__ == "__main__":
    main()
