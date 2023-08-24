from random import *
import json
def save():
    with open("order.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(order, ensure_ascii=False))
        print("Ваш заказ был принят в работу")
def load():
    with open("order.json", "r", encoding="utf-8") as fh:
        data = json.load(fh)
        print("Ваш заказ успешно загружен")
    return data

menu = []
order = []
menu.append('Паста Карбонара')
menu.append('Стейк из семги')
menu.append('Каре ягненка')
menu.append('Свиные медальоны')
menu.append('Скрэмбл с зеленью')
menu.append('Классический омлет')
menu.append('Цезарь с курицей')
menu.append('Салат из свежих овощей')
menu.append('Морковный пирог')
# try:
#     with open("menu.json", "r", encoding="utf-8") as fh:
#         menu = json.load(fh)
#         print("Ваш ассортимент успешно загружен")
# except:
#     menu.append('Окорок свиной')
#     menu.append('Лопатка свиная')
#     menu.append('Шея свиная')
#     menu.append('Карбонад свиной')
print('Добрый день! Вас приветствует сервис предварительного заказа нашего ресторана.')
while True:
    command = input("Введите команду:\n ")
    if command == '/start':
        print("Сервис начал работу")
    elif command == "/stop":
        print("Сервис остановил работу. До новых встреч!")
        break
    elif command == "/menu":
        print("Меню на сегодня:")
        list2 = [print(i) for i in menu]
    elif command == "/add":
        dish_name = input("Введите название блюда:\n")
        order.append(dish_name)
        print("Блюдо успешно добавлено в ваш заказ!")
    elif command == "/help":
        print("Официант уже идет к Вам!")
    elif command == "/del":
        dish_for_del = input("Введите название блюда, которое нужно удалить из заказа:\n")
        if dish_for_del in order:
            order.remove(dish_for_del)
            print("Блюдо удалено из заказа")
        else:
            print("Такого блюда нет в заказе!")

        # try:
        #     order.remove(dish_for_del)
        #     print("Блюдо удалено из заказа")
        # except:
        #     print("Такого блюда нет в заказе!")
    elif command == "/random":
        rnd_dish = choice(menu)
        print("Результат случайного выбора -" + rnd_dish)
    elif command == "/save":
        save()
    elif command == "/load":
        order = load()
    elif command == "/order":
        print('Ваш заказ:')
        list1 = [print(i) for i in order]
    else:
        print("Неопознанная команда. Просьба ввести команду еще раз или позвать официанта командой /help")
