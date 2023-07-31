# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
equation_1: str = "2*x^2 + 4*x + 5 = 0"
equation_2: str = "5*x^3 - 3*x^2 - 12 = 0"

def get_dictionary(equation: str) -> list:
    res_dict: list = list(equation.split())
    temp_list: list = []
    for i in range(len(res_dict)):
        if "^" in res_dict[i]:
            temp_list.append(res_dict[i].split('*x^'))
        if "^" not in res_dict[i] and "*x" in res_dict[i]:
            temp_list.append(res_dict[i].split('*x'))
        if res_dict[i] == "+":
            continue       
        if res_dict[i] == "-":
            temp_list.append(res_dict[i])
        if res_dict[i] == '0':
            continue      
        try:
            temp_list.append(int(res_dict[i]))
        except:
            continue       
    for i in range(len(temp_list)):
        if temp_list[i] == '-':
            try:
                temp_list[i + 1][0] = int(temp_list[i + 1][0])*-1
            except:
                temp_list[i + 1] = temp_list[i + 1]*-1
            
    print(temp_list)
            
get_dictionary(equation_1)