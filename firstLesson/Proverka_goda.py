# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# остальные годы, номер которых кратен 4, — високосные[5];
# все остальные годы — невисокосные.


VISOKOSNII = "Високосный"
NEVISOKOSNII = "Невисокосный"


def verify_year(y):
    if (y % 400) == 0:
        return VISOKOSNII
    elif (y % 100) == 0:
        return NEVISOKOSNII
    elif (y % 4) == 0:
        return VISOKOSNII
    else:
        return NEVISOKOSNII


print(verify_year(int(input("Введите год: "))))
