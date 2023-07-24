# задача Де моргана необязательная
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!
from random import choice
from random import randrange
from time import time

count = 0
start_time = time()
while count < 100:
    predicate_quality = randrange(3, 16)
    i = 0
    predicate_list = []
    while i <= predicate_quality:
        predicate_list.append(choice([True, False]))
        i += 1
    count += 1
    print(predicate_list)    
    temp = True
    temp_2 = False
    for item in predicate_list:
        if item == True:
            continue
        else:
            temp = item
            temp_2 = not item
    left_expression = temp
    right_expression = temp_2
    if not left_expression == right_expression:
        print('Верно')
    else:
        print('Не верно')    
end_time = time()  
print(f"На выполнение программы потрачено {round(end_time - start_time, 4)} секунд.")      