line1 = "2/5"
line2 = "3/4"
zn1 = int(line1[2])
zn2 = int(line2[2])


def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(m // (a + b))
    return m // (a + b)


nook = nok(zn1, zn2)
dpm1 = nook/zn1
dpm2 = nook/zn2

chisl1 = int(line1[0]) * dpm1
chisl2 = int(line2[0]) * dpm2

summa = chisl1 + chisl2
print(f"{int(summa)} / {int(dpm1*zn1)}")

ch1 = int(line1[0])
ch2 = int(line2[0])

ch = ch1*ch2
zn = zn1*zn2

print(f"{int(ch)} / {int(zn)}")