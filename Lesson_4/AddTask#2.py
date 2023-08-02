# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
equation_1: str = "x^2 + 4*x + 5 = 0"
equation_2: str = "5*x^3 - 3*x^2 - x + 12 = 0"

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
        
equation_list_1 = get_temp_list(equation_1)
equation_list_2 = get_temp_list(equation_2)

def get_dictionary(data_list):
    res_dict = {}
    for i in data_list:
        if "*x^" in i:
            res_dict[i] = i.split('*x^')
            res_dict[i][0] = int(res_dict[i][0])
            res_dict[i][1] = int(res_dict[i][1])
        elif "*x" in i:
            res_dict[i] = i.split('*x')
            res_dict[i][0] = int(res_dict[i][0])
            res_dict[i][1] = int(res_dict[i][1] + '0')
        elif "x^" in i:    
            res_dict[i] = i.split('x^')
            res_dict[i][0] = int(res_dict[i][0] + '1')
            res_dict[i][1] = int(res_dict[i][1])
        elif "x" in i:    
            res_dict[i] = i.split('x')
            res_dict[i][0] = int(res_dict[i][0] + '1')
            res_dict[i][1] = int(res_dict[i][1] + '0')
        else:
            res_dict[i] = i.split()
            res_dict[i][0] = int(res_dict[i][0])
    resut_list = [v for k, v in res_dict.items()]
    for i in resut_list:
        if len(i) > 1:
            i[0],i[1] = i[1],i[0]
    print(resut_list)      
    return resut_list

res_list_1 = get_dictionary(equation_list_1)
res_list_2 = get_dictionary(equation_list_2)

def get_max_pow(list_1: list, list_2: list) -> int:
    max_pow: int = max(list_1[0][0], list_2[0][0])
    return max_pow


pow: int = get_max_pow(res_list_1, res_list_2)
print(pow)

def get_main_list(list_1, list_2, max_pow):
    main_list = list_1 + list_2
    base_list = []
    last_el = 0
    first_el = 0
    for i in range(len(main_list)):
        if len(main_list[i]) == 1:
            last_el += main_list[i][0]            
        if main_list[i][0] == max_pow:
            first_el += main_list[i][1]
            
        # elif main_list[i][0]    
    base_list.append(first_el)
    base_list.append(last_el)        
   
    print(main_list)    
    print(base_list)    

get_main_list(res_list_1, res_list_2, pow)





# def get_list(equation: str) -> list:
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
#     for i in temp_list:
#         if i == '-':
#             temp_list.remove(i)
#     return temp_list








# def get_result_list(list_1: list, list_2: list) -> list:
#     temp_list: list = list_1 + list_2
#     result_list = []
#     for i in range(len(temp_list)):
#         if type(temp_list[i]) == list and type(temp_list[i+1]) == list and i[1] == j[1]:
#             result_list.append(int(i[0]) + int(j[0]))





