# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка
# содержит число X
# Пример: 
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
len_list = int(input("Введите длину массива:\n"))
user_list = []
for _ in range(len_list):
    user_list.append(randint(1, len_list))    
user_list = sorted(user_list)
print(user_list)
number_search = int(input("Введите искомое число:\n"))
for item in user_list:
    if item == number_search:
        print(item)
        break
    elif (number_search > item and item == max(user_list)) or (number_search < item and item == min(user_list)):
        print(item)
        break
    elif number_search < max(user_list) and number_search > min(user_list):
        if item - number_search > 0: 
            print(item)
            break
# Решение:
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)        