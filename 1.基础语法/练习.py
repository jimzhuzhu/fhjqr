ls = range(100, 1000)
for i in ls:
    temp = list(str(i))
    a = temp[0]
    b = temp[1]
    c = temp[2]
    if a**3 + b**3 + c**3 == i:
        print(i)
