"""
Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

start_sum = 0


def operations(start_money):
    counter = 1
    while True:
        menu = int(input("1.Пополнить\n"
                         "2.Снять\n"
                         "3.Выход\n"))
        if start_money > 5000000:
            start_money -= start_money*0.1
        if menu == 1:
            start_money += get_money()
            print(start_money)
        elif menu == 2:
            take_sum = get_money()
            if take_sum > start_money:
                print("Сумма превышает остаток на счете \n", start_money)
                continue
            start_money -= take_procent(take_sum)
            print(start_money)
        elif menu == 3:
            break
        else:
            print("Нет такой команды")
            print(start_money)
        if counter % 3 == 0:
            print("x",counter)
            start_money += start_money*0.03
        counter += 1


def get_money():
    money = int(input("Введите сумму: "))
    if (money % 50) != 0:
        print("Сумма должна быть кратна 50 у.е ")
        return 0
    return money


def take_procent(money_sum):
    procent = money_sum * 0.015
    if procent < 30:
        procent = 30
    elif procent > 600:
        procent = 600
    return procent


operations(start_sum)
