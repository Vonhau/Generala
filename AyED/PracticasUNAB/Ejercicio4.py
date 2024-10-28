"""Ejercicio 4

4.1-Agregar a la clase Comprador un metodo lista a string que devuelva una lista de strings con los atributos de los articulos comprados identificador,
 nombre, marca, precio, puntos) separados por puntos y comas (ej: [1; "computadora","dell", 100.00, 30, 5, "mouse": "logitech": 200.00; 15])

4,2-Escribir una función que reciba la lista de compradores creada en el punto 3.2 y genere archivos de texto con extensión.csv
 cuyo nombre sea el nombre del comprador y que contengan la lista de articulos correspondiente, un articulo en cada linea
"""

from Ejercicio3 import NewBuyer, Article, bubble_sort
import csv


class NewNewBuyer(NewBuyer):
    def __init__(self, name, address, phone, email, birth_date):
        super().__init__(name, address, phone, email, birth_date)

    def articles_to_string_list(self):
        return [f"Id: {article.id}; Name: {article.name}; Mark: {article.mark}; Price: {article.price}; Points: {article.points}"
                for article in self.get_buyed_articles()]


def generate_buyers_text(buyers):
    for buyer in buyers:
        with open(f"{buyer.name}.csv", "w", newline='', encoding='utf-8') as archive:
            writer = csv.writer(archive)
            writer.writerow(["id", "name", "desc", "mark", "price", "points"])
            for article in buyer.get_buyed_articles():
                writer.writerow([article.id, article.name, article.description,
                                article.mark, article.price, article.points])


def main():
    # Creamos los compradores
    buyer1 = NewNewBuyer("Joako", "Avenida Falsa 123",
                         "123 123 123", "joateixido15@gmail.com", "11/06/2006")
    buyer2 = NewNewBuyer("Matias", "Avenida Falsa 124",
                         "123 123 123", "matias15@gmail.com", "12/06/2007")
    buyer3 = NewNewBuyer("Pepito", "Avenida Falsa 125",
                         "123 123 123", "pepito15@gmail.com", "09/07/2006")
    buyer4 = NewNewBuyer("Juancito", "Avenida Falsa 126",
                         "123 123 123", "juancito15@gmail.com", "18/03/2003")
    buyer5 = NewNewBuyer("Santiago", "Avenida Falsa 127",
                         "123 123 123", "santiago15@gmail.com", "11/03/2004")
    buyer6 = NewNewBuyer("Alex", "Avenida Falsa 128",
                         "123 123 123", "alex15@gmail.com", "01/05/2008")
    # Creamos la lista de compradores
    buyers = [buyer1, buyer2, buyer3, buyer4, buyer5, buyer6]
    # Creamos los articulos
    article1 = Article(1, "Remera", "Es de algodon", "Jaguar", 16.67, 25)
    article2 = Article(2, "Pantalon", "Es de tela", "Rusty", 14.77, 20)
    article3 = Article(3, "Buzo", "Es de cuero", "New Age", 20.54, 35)
    # Los compradores compran articulos
    buyer1.buy_article(article1)
    buyer1.buy_article(article2)
    buyer2.buy_article(article3)
    buyer3.buy_article(article3)
    buyer4.buy_article(article1)
    buyer5.buy_article(article1)
    buyer6.buy_article(article2)
    # Chequeamos que el comprador tenga los articulos
    print(buyer1.get_buyer())
    # Llamamos a la funcion que nos permite pasar los articulos a strings
    print(buyer1.articles_to_string_list())
    # Generamos los archivos de texto en base a los datos de los articulos
    generate_buyers_text(buyers)


if __name__ == "__main__":
    main()
