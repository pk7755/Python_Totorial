# import array as arr
from array import *
arr = array('i',[])
n = int(input("Enter the size of array : "))
for i in range(n):
    x = int(input("Enter the next value : "))
    arr.append(x)
print(arr)
e=int(input("Enter the value for search : "))
k=0
for value in arr:
    if e == value:
        print("The index of ", e ," is ",k," .")
        break
    k+=1
else:
    print("Not found..!")



    