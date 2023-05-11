from numpy import *

# ----------------array()-------------------------
arr = array([1, 2, 3, 4, 5, 5])
arr2 = array([6, 5, 4, 3, 5, 4])

# it will increase by 6 in each element
arr = arr + 6
# it will give the summation of both array if the both array having the same no of elements
arr3 = arr+arr2

# it will give the log value of each element
arr4 = log(arr3)

# it will give the square root of each element in the array
arr5 = sqrt(arr3)

# mathematical operations
arr6 = sum(arr3)
arr7 = min(arr3)
arr8 = max(arr3)
# print(arr6)
# print(arr7)
# print(arr8)


# it will concatenate the two  or more arrays
arr9 = concatenate([arr2, arr3])

# copy the array , this will generally share the address of arr9 to the arr10
arr10 = arr9

if id(arr10)==id(arr9) :
    print("The address of both array is same")
else:
    print("The address of both array is different")

# this will create an array view with different location 
# Shallow copy : if you are going to make changes in any element of the first array than these change will also reflect on it shallow copy
arr11 = arr9.view()
if id(arr11)==id(arr9) :
    print("The address of both array is same")
else:
    print("The address of both array is different")

# this will create an array view with different location 
# deep copy
arr12 = arr9.copy()
if id(arr12)==id(arr9) :
    print("The address of both array is same")
else:
    print("The address of both array is different")

print(arr12)

