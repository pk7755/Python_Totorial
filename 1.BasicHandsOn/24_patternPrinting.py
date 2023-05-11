n=9

for i in range(0,n,1):
    num=1
    for j in range(n-i):
            print(" ",end="")
    for k in range(i):
            print(num, end=" ")
            num+=1
    print()
