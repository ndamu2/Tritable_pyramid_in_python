print("second number pattern")

lastNum=15
for i in range(1,lastNum):
    for j in range(-1+i, -1, -1):
        print(format(j * i, "5d"),end='')
    print("")
