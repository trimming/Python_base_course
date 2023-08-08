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
from checkMatch import check_match
area = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
game = True
move = True
count = 0
while game and count < 9:
        if move:
                row = int(input("Введите номер строки:\n"))
                column = int(input("Введите номер столбца:\n"))
                move = False
                area[row-1][column-1] = 'X'
                count += 1
                print(*area[0], sep = ' | ')
                print(*area[1], sep = ' | ')
                print(*area[2], sep = ' | ')
                print()
                game = check_match(area[row-1][column-1],area)
        else:
                free_or_busy = True
                while free_or_busy and count < 100:
                        row = randint(1, 3)
                        column = randint(1, 3)
                        if area[row-1][column-1] == ' ':
                                area[row - 1][column - 1] = 'O'
                                free_or_busy = False
                                print(*area[0], sep = ' | ')
                                print(*area[1], sep = ' | ')
                                print(*area[2], sep = ' | ')
                                game = check_match(area[row-1][column-1],area)
                        else:
                                free_or_busy = True
                move = True
                count += 1
if count == 9 and game == True:
    print("Ничья!")

