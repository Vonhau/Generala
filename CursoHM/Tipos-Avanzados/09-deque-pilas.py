import timeit
from collections import deque


def inser_elements():
    numbers = deque()

    for element in range(0, 100_000):
        numbers.appendleft(element)


if __name__ == '__main__':
    result = timeit.timeit(inser_elements, number=1)
    print(result)
