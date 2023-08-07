# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например:
# |     |  Х |
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
from random import randint
import os
area = [[[],[],[]],
        [[],[],[]],
        [[],[],[]]]
print(f" {area[0]}\n {area[1]}\n {area[2]}")
game = True
move = True
while game:
        if move:
                row = int(input("Введите номер строки:\n"))
                column = int(input("Введите номер столбца:\n"))
                move = False
                area[row-1][column-1] = 'X'
                print(f" {area[0]}\n {area[1]}\n {area[2]}")
                if ((area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X')
                        or (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X')
                        or (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X')
                        or (area[0][0] == 'X' and area[1][0] == 'X' and area[1][0] == 'X')
                        or (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X')
                        or (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X')
                        or (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X')
                        or (area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X')):
                        print("Игра окончена, вы выиграли!")
                        game = False



        else:
                count = 1
                free_or_busy = True
                while free_or_busy:
                        row = randint(1, 3)
                        column = randint(1, 3)
                        if area[row-1][column-1] == []:
                                area[row - 1][column - 1] = 'O'
                                free_or_busy = False
                                print(f" {area[0]}\n {area[1]}\n {area[2]}")
                        else:
                                free_or_busy = True
                                count += 1
                move = True
