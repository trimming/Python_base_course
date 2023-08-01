# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
equation_1: str = "2*x^2 + 4*x + 5 = 0"
equation_2: str = "5*x^3 - 3*x^2 - 12 = 0"

# def get_dictionary(equation: str) -> list:
#     res_dict: list = list(equation.split())
#     temp_list: list = []
#     for i in range(len(res_dict)):
#         if "^" in res_dict[i]:
#             temp_list.append(res_dict[i].split('*x^'))
#         if "^" not in res_dict[i] and "*x" in res_dict[i]:
#             temp_list.append(res_dict[i].split('*x'))
#         if res_dict[i] == "+":
#             continue       
#         if res_dict[i] == "-":
#             temp_list.append(res_dict[i])
#         if res_dict[i] == '0':
#             continue      
#         try:
#             temp_list.append(int(res_dict[i]))
#         except:
#             continue       
#     for i in range(len(temp_list)):
#         if temp_list[i] == '-':
#             try:
#                 temp_list[i + 1][0] = int(temp_list[i + 1][0])*-1
#             except:
#                 temp_list[i + 1] = temp_list[i + 1]*-1
            
#     print(temp_list)
def get_temp_list(equation):
    temp_list = equation.split()
    j = 0
    for i in temp_list:
        if (i == "+") or (i == "="):
            temp_list.remove(i)
        if i == "-":
            temp_list[j + 1] = "-" + temp_list[j + 1]
            temp_list.remove(i)
        j += 1
    temp_list.pop()                            
    return temp_list            
equation_list = get_temp_list(equation_2)

def get_dictionary(data_list):
    res_dict = {}
    for item in res_dict:
        for key, value in item.items():
            if 
            print(data_list)

get_dictionary(equation_list)
user_equation_1: str = "2*x^3 + 4*x^2 + 5x = 0"
user_equation_2: str = "5*x^3 - 3*x^2 - 12 = 0"


def get_list(equation: str) -> list:
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
    for i in temp_list:
        if i == '-':
            temp_list.remove(i)
    return temp_list


list_equation_1: list = get_list(user_equation_1)
list_equation_2: list = get_list(user_equation_2)
print(list_equation_1)
print(list_equation_2)


def get_max_pow(list_1: list, list_2: list) -> int:
    max_pow: int = max(list_1[0][1], list_2[0][1])
    return int(max_pow)


pow: int = get_max_pow(list_equation_1, list_equation_2)
print(pow)


def get_result_list(list_1: list, list_2: list) -> list:
    temp_list: list = list_1 + list_2
    result_list = []
    for i in range(len(temp_list)):
        if type(temp_list[i]) == list and type(temp_list[i+1]) == list and i[1] == j[1]:
            result_list.append(int(i[0]) + int(j[0]))

    # for i in list_1:
    #     for j in list_2:
    #         if type(i) == list and type(j) == list and i[1] == j[1]:
    #             result_list.append(int(i[0]) + int(j[0]))
    #         if type(i) == list and type(j) == list and i[1] == '':
    #             result_list.append(int(i[0]))
    #         if type(i) == int and type(j) == int:
    #             result_list.append(i + j)
    print(temp_list)


get_result_list(list_equation_1, list_equation_2)
