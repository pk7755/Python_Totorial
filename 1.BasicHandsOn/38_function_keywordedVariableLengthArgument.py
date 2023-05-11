# Variable length argument 

# Keyword variable length argument
def person(name, **data):
    print("Name is :", name)
    for i, j in data.items():
        print(i, " is :", j)


person('Pradyumna', age=22, city='Ghazipur', mobile=2345678654)
