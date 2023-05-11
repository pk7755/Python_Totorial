# Variable length argument
def sum1(a, *b):
    c = a
    for i in b:
        c += i
    print(c)


sum1(3, 4, 5, 6, 6, 5)

