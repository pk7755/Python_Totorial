def fib(a, b, n):
    ls = [a, b]
    for i in range(n):
        c = a + b
        a = b
        b = c
        ls.append(c)
    return ls


n = int(input('Please Enter the length of the fibonacci series : '))
a = int(input('Enter the starting element of series : '))
b = int(input('Enter the second element of series : '))
fibonacci_Series = fib(a, b, n)
print(fibonacci_Series)


