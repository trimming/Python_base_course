# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import randint
def get_list_indexes(data_list):
    list1 =[data_list.index(i) for i in data_list if i < max and i > min]
    return list1
data_list = [randint(-10, 500) for _ in range(10, 30)]
min = 1
max = 200
print(get_list_indexes(data_list))