# import array as arr
from array import *
val = array('i',[3,4,7,3,2,5])

newArr = array(val.typecode, (a for a in val))
newArr1 = array(val.typecode, (a*a for a in val))



for i in newArr1:
    print(i)


    