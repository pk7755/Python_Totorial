def topten():
    n = 1
    
    while n <= 10:
        yield n
        n += 1

def toptenSq():
    n = 1
    
    while n <= 10:
        
        yield n*n
        n += 1

value = topten()
sqs = toptenSq()

for i in value:
    print(i)

for i in sqs:
    print(i)