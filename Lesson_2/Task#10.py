from random import choice
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
n = int(input("Количество монет:\n"))
count = 0
coins_list = []
while count < n:
    coins_list.append(choice([0, 1]))
    count += 1
print(coins_list)
coins_1 = 0
coins_0 = 0
for i in coins_list:
    if i == 0:
        coins_0 += 1
    else:
        coins_1 += 1
if coins_1 <= coins_0:
    print(f"Нужно перевернуть {coins_1} монеты")
else:
    print(f"Нужно перевернуть {coins_0} монеты")                
