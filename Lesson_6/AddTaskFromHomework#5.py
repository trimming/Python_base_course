# Задача 1 необязательная. Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7;
#     (1+2)*3 => 9;
# Тут может помочь библиотека re
import re
def result_expression(string):
    match = re.search(r'\D', string)
    if match == None:        
        return int(string)
    if match[0] == '+':
        temp = string.split('+',1)
        res = int(temp[0]) + result_expression(temp[1])        
    if match[0] == '*':
        temp = string.split('*',1)
        res = int(temp[0]) * result_expression(temp[1])        
    if match[0] == '/':
        temp = string.split('/',1)
        res = int(temp[0]) // result_expression(temp[1])        
    if match[0] == '-':
        temp = string.split('-',1)
        res = int(temp[0]) - result_expression(temp[1])             
    return res       
print(result_expression("6-4/2"))