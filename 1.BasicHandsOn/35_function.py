def update(x):
    print(id(x))
    x[0] = 8
    print(id(x))
    print("x ", x)


a = [10]
print(id(a))
update(a)
print("a ", a)

# this method is pass by reference here that is possible because in the python list are mutable,
# we can change the value at the same memory address

