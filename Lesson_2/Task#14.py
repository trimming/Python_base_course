# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
N = int(input("Введите число\n"))
pow_number = 1
while pow_number < N:
    print(pow_number)
    pow_number = pow_number * 2
    