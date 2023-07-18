number = int(input("Введите десятичное число: "))
print(hex(number))
hex_digit = "0123456789ABCDEF"
hex_number = ""

while number > 0:
    remainder = number % 16
    hex_number = hex_digit[remainder] + hex_number
    number //= 16
print(hex_number)

