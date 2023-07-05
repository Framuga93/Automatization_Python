def elka_print(ryad):
    indent = ryad - 1
    zvezda = 1
    for i in range(ryad):
        print((" " * indent) + ("*" * zvezda) + (" " * indent))
        indent -= 1
        zvezda += 2


elka_print(int(input("Введите кол-во рядов: ")))
