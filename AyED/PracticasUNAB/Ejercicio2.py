"""2.1-Agregar a la clase Comprador un método comprar articulo que permita adquirir Articulos y agregarlos
 a una lista (privada) de articulos comprados.
 Al comprarios, los puntos del artículo se suman a los puntos del Comprador. 

2.2-Agregar a la clase Comprador un método encontrar articulo que reciba el identificador del articulo
 y devuelva True o False de acuerdo a si el artículo está o no en la lista del comprador.
   Utilizar el método de búsqueda lineal 

2.3-Agregar a la clase Comprador un método eliminar articulo que reciba el identificador del artículo 
y elimine TODAS las instancias del articulo en la lista del comprador. En cada ocasión,
 deben eliminarse los puntos correspondientes al artículo del puntaje del comprador
"""
from Ejercicio1 import Buyer, Article


class NewBuyer(Buyer):
    def __init__(self, name, address, phone, email, birth_date):
        super().__init__(name, address, phone, email, birth_date)
        self.__buyed_articles = []

    def buy_article(self, article):
        self.__buyed_articles.append(article)
        self.add_score(article.points)

    def find_article(self, identifier):
        for article in self.__buyed_articles:
            if article.id == identifier:
                return True
        return False

    def remove_article(self, identifier):
        articles_to_remove = [
            article for article in self.__buyed_articles if article.id == identifier]
        self.__buyed_articles = [
            article for article in self.__buyed_articles if article.id != identifier]

        for article in articles_to_remove:
            self.remove_score(article.points)

    def get_buyer(self):
        article_names = [article.name for article in self.__buyed_articles]
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}, Birth Date: {self.birth_date}, Score: {self.score}, Buyed Articles: {article_names}"

    def get_buyed_articles(self):
        return self.__buyed_articles


def main():
    buyer1 = NewBuyer("Joako", "Avenida Falsa 123",
                      "123 123 123", "joateixido15@gmail.com", "11/06/2006")
    article1 = Article(1, "Remera", "Es de algodon", "Jaguar", 16.67, 25)
    article2 = Article(2, "Pantalon", "Es de tela", "Rusty", 14.77, 30)
    print(f"Datos del comprador antes de comprar: {buyer1.get_buyer()}")
    buyer1.buy_article(article1)
    print(f"Datos del comprador despues de comprar: {buyer1.get_buyer()}")
    print(f"El articulo 1 del comprador {
          buyer1.name} fue encontrado: {buyer1.find_article(1)}")
    print(f"El articulo 2 del comprador {
          buyer1.name} fue encontrado: {buyer1.find_article(2)}")
    buyer1.remove_article(article1.id)
    print(f"Datos del comprador despues de remover articulo: {
          buyer1.get_buyer()}")


if __name__ == "__main__":
    main()
