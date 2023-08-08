def check_match(cell, area):
    if ((area[0][0] == cell and area[0][1] == cell and area[0][2] == cell)
            or (area[1][0] == cell and area[1][1] == cell and area[1][2] == cell)
            or (area[2][0] == cell and area[2][1] == cell and area[2][2] == cell)
            or (area[0][0] == cell and area[1][0] == cell and area[2][0] == cell)
            or (area[0][1] == cell and area[1][1] == cell and area[2][1] == cell)
            or (area[0][2] == cell and area[1][2] == cell and area[2][2] == cell)
            or (area[0][0] == cell and area[1][1] == cell and area[2][2] == cell)
            or (area[0][2] == cell and area[1][1] == cell and area[2][0] == cell)):

        if cell == 'X':
            print("Игра окончена, вы выиграли!")
        else:
            print("Игра окончена, вы проиграли!")
        return False
    else:
        return True
