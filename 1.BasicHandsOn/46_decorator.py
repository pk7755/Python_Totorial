

def div(a, b):
    print(a / b)

# here we are adding new features in the function without touching the main function body
# which in known as decorators


def update_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = update_div(div)

div(2, 4)
