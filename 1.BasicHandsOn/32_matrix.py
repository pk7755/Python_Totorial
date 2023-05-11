from numpy import * 

arr = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# converting an array into matrix
m = matrix(arr)

# creating matrix 
m1 = matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
m2 = matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')

# Arithmetic operation on matrix
print(m1+m2)
print(m1-m2)
print(m1*m2)
print(m1/m2)


# Printing the diagonal element of any matrix
print(diagonal(m1))

print(m1.min())
print(m1.max())
print(m1.sum())



print(m1)

