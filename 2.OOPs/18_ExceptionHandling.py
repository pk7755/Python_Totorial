
try:
    a = 10
    b = 0
    result = 0
    print("connection open")
    result = a/b
    print(result)
except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except NameError as e:
    print(e)

except Exception as e:
    print(e)

finally:    
    print("connectio close")

