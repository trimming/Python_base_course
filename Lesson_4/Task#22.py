# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint
elements_quantity_1: int = int(input("Введите количество элементов первого множества:\n"))
elements_quantity_2: int = int(input("Введите количество элементов второго множества:\n"))
def get_set_numbers(number_1: int, number_2: int):
    list_1: list = [randint(1, 20) for _ in range(number_1)]
    list_2: list = [randint(1, 20) for _ in range(number_2)]
    score_1: set = set(list_1)
    score_2: set = set(list_2)
    score: set = score_1.intersection(score_2)

    print(*list_1)
    print(*list_2)
    print(*score)
get_set_numbers(elements_quantity_1, elements_quantity_2)    