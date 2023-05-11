

def fib(a, b, n):
    print(a, end=" ")
    print(b, end=" ")

    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c, end=" ")


n = int(input('Please Enter the length of the fibonacci series : '))
a = int(input('Enter the starting element of series : '))
b = int(input('Enter the second element of series : '))
fib(a, b, n)

