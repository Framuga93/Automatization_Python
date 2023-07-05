"""
Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено:
цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25 Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""


def input_and_option_number():
    number = input("Введите число: ")
    quantity_num(number)


def quantity_num(num):
    if len(num) == 1 and int(num) != 0:
        return int(num) ** 2
    elif len(num) == 2:
        return int(num[0]) + int(num[1])
    elif len(num) == 3:
        return int(num[2] + num[1] + num[0])
    else:
        input_and_option_number()


print(input_and_option_number())
