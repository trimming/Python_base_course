# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A. Последняя строка содержит число X
# Пример: 
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint
len_list = int(input("Введите длину массива:\n"))
user_list = []
for _ in range(len_list):
    user_list.append(randint(1, len_list))    
print(user_list)
number_search = int(input("Введите искомое число:\n"))
count = 0
for item in user_list:
    if item == number_search:
        count += 1
if count > 0:          
    print(f"Искомое число встречается {count} раз")        
else:
    print("Искомого числа нет в массиве")    