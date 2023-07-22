# задача 1 сложная необязательная Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.
from decimal import Decimal
number = Decimal(input("Введите число:\n"))
sum = 0
rest = 0
while number >= 1 or number <= -1:
    sum += number % 10
    number = number // 10
rest = sum - int(sum)      
sum = sum - rest    

while rest != 0:
    rest = rest * 10
    sum += int(rest) // 1
    rest -= int(rest) 
if number < 1 and number > -1:
    rest = number
    while rest != 0:
        rest = rest * 10
        sum += int(rest) // 1
        rest -= int(rest)    
print(sum)