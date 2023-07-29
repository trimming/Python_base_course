# задача 1 необязательная. Напишите программу, которая получает целое число и 
# возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции
user_number: int = int(input("Введите целое число для преобразования:\n"))
def get_binar_number(number: int) -> str:
    binar: str = ''
    if number == 0:
        return '0'
    while number > 0:
        binar = str(number % 2) + binar
        number = number // 2
    return binar

def get_octal_number(number: int) -> str:
    octal: str = ''
    if number == 0:
        return '0'
    while number > 0:
        octal = str(number % 8) + octal
        number = number // 8        
    return octal
print(f"Двоичное представление: {get_binar_number(user_number)}, восьмеричное представление: {get_octal_number(user_number)}")    