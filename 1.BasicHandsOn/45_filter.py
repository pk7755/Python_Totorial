from functools import *
def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


ls = [2, 3, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7]
evens = list(filter(is_even, ls))
odds = list(filter(is_odd, ls))
print(odds)
print(evens)


even = list(filter(lambda a: a % 2 == 0, ls))
print(even)

sum = reduce(lambda a, b: a + b, ls)
print(sum)
