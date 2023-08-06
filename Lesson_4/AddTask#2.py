# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re

def get_temp_list(equation): # Эта функция разделяет строку многочлена на элементы, удаляет +, = и 0, 
    temp_list = equation.split() # а также если есть - меняет знак числа. Возвращает список с элементами многочлена.
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
        

def get_dictionary(data_list):# Эта функция принимает список сложенный из двух списков элементов многочленов, 
    dictionary = {} # составляет словарь, в котором ключом является степень, возвращает этот словарь.
    for i in data_list:
        if "*x^" in i:
            el = i.split("*x^")
            key = int(el[1])
            if key not in dictionary:
                dictionary[key] = [int(el[0])]
            else:
                dictionary[key].append(int(el[0]))
        elif "*x" in i:
            el = i.split("*x")
            key = 1
            if key not in dictionary:
                dictionary[key] = [int(el[0])]
            else:
                dictionary[key].append(int(el[0]))
        elif "x^" in i:
            el = i.split("x^")
            key = int(el[1])
            if key not in dictionary:
                dictionary[key] = [int(el[0] + '1')]
            else:
                dictionary[key].append(int(el[0]))
        elif "x" in i:
            el = i.split("x")
            key = 1
            if key not in dictionary:
                dictionary[key] = [int(el[0] + '1')]
            else:
                dictionary[key].append(int(el[0] + '1'))
        else:
            el = (i + ' 0').split(' ')
            key = int(el[1])
            if key not in dictionary:
                dictionary[key] = [int(el[0])]
            else:
                dictionary[key].append(int(el[0]))              
    return dictionary

def get_result_list(data_dict):# Эта функция из словаря получает множетели и сохраняет их в список по принципу 
    base_list = [] # соотношения ключа-степени индексу списка
    temp = list(data_dict)
    temp.sort(reverse=True)
    for i in temp:        
        base_list.append(sum(data_dict[i]))    
    return base_list

def get_result(base_list):# В этой функции составляем результирующий многочлен
    result = ""
    k = len(base_list) - 1
    for i in base_list:
        if i == 0:
            continue
        elif i == 1 and k > 1:                
            result += f"x^{k}"
        elif i == 1 and k == 1:                    
            result += f"x"    
        else:         
            if k == 0:
                if i > 0:                
                    result += f"+{i}"
                else:
                    result += f"{i}"    
            elif k == 1:                
                result += f"{i}*x"
            else:               
                result += f"{i}*x^{k}"
        k -= 1    
    result += " = 0"
    print(result)

equation_1: str = "2x^3 + x^2 + 5 = 0"
equation_2: str = "5x^3 - 2x^2 - x + 12 = 0"

res_dictionary = get_dictionary(get_temp_list(equation_1) + get_temp_list(equation_2))

get_result(get_result_list(res_dictionary))


