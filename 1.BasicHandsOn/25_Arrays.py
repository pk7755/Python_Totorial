# import array as arr
from array import *
val = array('i',[3,4,7,3,2,5])
print(val)
print(val.buffer_info())
print(val.typecode)
val.reverse()
print(val)


for i in val:
    print(i)