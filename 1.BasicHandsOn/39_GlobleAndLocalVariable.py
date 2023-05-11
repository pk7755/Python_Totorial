# Variable length argument 

a = 10
print(id(a))
print("global outside func : ", a)


def any1():
    a = 9
    # to get the global variable reference
    x = globals()['a']
    print("global inside func : ", x)
    print(id(x))
    print(a)


any1()
