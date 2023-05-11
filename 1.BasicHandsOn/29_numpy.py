from numpy import *

#----------------array()-------------------------
arr = array([1,2,3,4,5,5])
arr = array([1,2,3,4,5,5],int)


# ----------------linspace(start,end,part)---------------------
# it will create the 20 partition in the range of 0 to 15
arr1 = linspace(0,15,20)
# if you are not define the no of parts which is the third argument in that method 
# than it will create 50 part by default
arr2 = linspace(0,15)

# ----------------logspace(start,end,part)---------------------
# it will create the 20 partition in the range of 0 to 15 to the power of log
arr3 = logspace(0,15,20)
# if you are not define the no of parts which is the third argument in that method 
# than it will create 50 part by default
arr4 = logspace(0,15)

#-----------------arange(start,end,steps)------------------------
arr5 = arange(1,15,2)

#-----------------zeros(size)-----------------------------------
arr6 = zeros(5)
#-----------------ones(size)------------------------------------
arr7 = ones(5)

print(arr7)
