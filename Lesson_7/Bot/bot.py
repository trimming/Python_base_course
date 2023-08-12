from random import *
meat = []
meat.append('Окорок свиной')
meat.append('Лопатка свиная')
meat.append('Шея свиная')
meat.append('Карбонад свиной')
while True:
    command = input("Введите команду ")
    if command == '/start':
        print("Бот начал работу")
    elif command == "/stop":
        print("Бот остановил работу. До новых встреч!")
        break
    elif command == "/show":
        print("Вот текущий ассортимент")
        print(meat)
    elif command == "/add":
        m = input("Введите отруба:\n")
        meat.append(m)
        print("Отруб успешно добавлен в ассортимент!")
    elif command == "/help":
        print("Здесь какой-то мануал")
    elif command == "/del":
        m = input("Введите название отруба который нужно удалить из ассортимента:\n")
        '''
        if m in meat:
            meat.remove(m)
            print("Отруб удален из ассортимента")
        else:
            print("Такого названия нет в разделке!")
        '''
        try:
            meat.remove(m)
            print("Отруб удален из ассортимента")
        except:
            print("Такого названия нет в разделке!")
    else:
        print("Неопознанная команда")
