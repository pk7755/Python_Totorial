from numpy import *

arr = array([
                [1, 2, 3, 1, 2, 3],
                [4, 5, 6, 1, 2, 3],
                            ])
print(arr)

# it will give the size of multi dimentational array
print(arr.shape)

# size treat the array like a 1D array show it will give you the size as the 1d array
print(arr.size)

# it will convert the multi dimenatational arrya into the one 1D array
arr3 = arr.flatten()
print(arr3.shape)

# -----------------reshape(row,column)-----------------
arr4 = arr3.reshape(3,4)


# Three dimentational array
arr5 = arr3.reshape(2,2,3)
print(arr5)
