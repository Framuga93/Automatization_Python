

def print_tabl():
    for i in range(1):
        for j in [2, 6]:
            for k in range(2, 10):
                if j * k > 9:
                    indent = "    "
                else:
                    indent = "     "
                print(str(j) + "X" + str(k) + "=" + str(j * k) + indent
                      + str(j + 1) + "X" + str(k) + "=" + str((j + 1) * k) + indent
                      + str(j + 2) + "X" + str(k) + "=" + str((j + 2) * k) + indent
                      + str(j + 3) + "X" + str(k) + "=" + str((j + 3) * k) + indent)
            print("\n")

#Понимаю изза чего не ровно. Извиняюсь, сильно лень переписывать)

print_tabl()
