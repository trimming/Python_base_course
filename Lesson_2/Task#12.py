# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
from math import sqrt
S = int(input("Введите сумму чисел:\n"))
P = int(input("Введите их произведение:\n"))
D = S * S - 4 * P
if D > 0:
    X = (S - sqrt(D)) // 2
    Y = (S + sqrt(D)) // 2
print(X, Y)    