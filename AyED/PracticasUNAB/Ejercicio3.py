"""Ejercicio 3

3.1-Crear seis instancias de compradores, y agregarles
 (mediante el método comprar articulos diferentes cantidades de articulos.
 Nota: crear las instancias necesarias do articulos diferentes.

3.2-Crear una lista con estos compradores

3.3-Utilizar el método de ordenamiento burbuja para ordenartos de forma DESCENDENTE
 (de mayor valor a menor valor) de acuerdo al puntaje de cada uno.

3.4-Crear una lista enlazada de todos los articulos creados en el punto 3.1, 
y escribir una función que pueda procesar esta lista y determinar
 (devolviendo un valor booleano)
 si existen dos articulos con la misma cantidad de puntos."""

from Ejercicio2 import NewBuyer, Article


class Node:
    def __init__(self, article):
        self.article = article
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_article(self, article):
        nodo = Node(article)
        if self.head is None:
            self.head = nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nodo

    def search_duplicated_points(self):
        article_points = {}
        current = self.head
        while current:
            points = current.article.points
            if points in article_points:
                return True
            article_points[points] = True
            current = current.next
        return False

# Creamos el ordenamiento burbuja DESCENDENTE


def bubble_sort(user_list):
    n = len(user_list)
    for i in range(n-1):
        for j in range(n-1-i):
            if user_list[j].score < user_list[j+1].score:
                user_list[j], user_list[j+1] = user_list[j+1], user_list[j]


def main():
    # Creamos los compradores
    buyer1 = NewBuyer("Joako", "Avenida Falsa 123",
                      "123 123 123", "joateixido15@gmail.com", "11/06/2006")
    buyer2 = NewBuyer("Matias", "Avenida Falsa 124",
                      "123 123 123", "matias15@gmail.com", "12/06/2007")
    buyer3 = NewBuyer("Pepito", "Avenida Falsa 125",
                      "123 123 123", "pepito15@gmail.com", "09/07/2006")
    buyer4 = NewBuyer("Juancito", "Avenida Falsa 126",
                      "123 123 123", "juancito15@gmail.com", "18/03/2003")
    buyer5 = NewBuyer("Santiago", "Avenida Falsa 127",
                      "123 123 123", "santiago15@gmail.com", "11/03/2004")
    buyer6 = NewBuyer("Alex", "Avenida Falsa 128",
                      "123 123 123", "alex15@gmail.com", "01/05/2008")
    # Creamos la lista de compradores
    buyers = [buyer1, buyer2, buyer3, buyer4, buyer5, buyer6]
    # Creamos los articulos
    article1 = Article(1, "Remera", "Es de algodon", "Jaguar", 16.67, 25)
    article2 = Article(2, "Pantalon", "Es de tela", "Rusty", 14.77, 20)
    article3 = Article(3, "Buzo", "Es de cuero", "New Age", 20.54, 35)
    article4 = Article(4, "Zapatilla", "Es de cuerina", "Converse", 30.70, 50)
    # Asignamos distintos elementos a cada comprador
    buyer1.buy_article(article1)
    buyer1.buy_article(article2)
    buyer2.buy_article(article3)
    buyer3.buy_article(article4)
    buyer3.buy_article(article3)
    buyer4.buy_article(article1)
    buyer4.buy_article(article4)
    buyer5.buy_article(article1)
    buyer6.buy_article(article2)
    # Llamamos al ordenamiento burbuja
    bubble_sort(buyers)
    print("Compradores ordenados por puntajes descendentes")
    for buyer in buyers:
        print(buyer.name, buyer.score)
    # Creamos la lista enlazada de articulos
    article_list = LinkedList()
    article_list.add_article(article1)
    article_list.add_article(article2)
    article_list.add_article(article3)
    article_list.add_article(article4)
    # Verificamos si existen articulos con la misma cantidad de puntos.
    print(f"Existen dos articulos con los mismos puntos: {
          article_list.search_duplicated_points()}")


if __name__ == "__main__":
    main()
