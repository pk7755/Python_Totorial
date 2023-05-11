list = [23,56,45,3,4,323,5,46,57,4]
print(list)

print(list[0])
print(list[0:])
print(list[3:])
print(list[2:4])
print(list[:3])
print(list[:(len(list))])


list.sort()
print(list)

list.insert(2,34)
print(list)

ls = list.copy();
print(ls)

ls.clear()
print(ls)

count=list.count(4)
print(count)

list.extend([1,2,3,4,5,6,54,3])
print(list)

print(list.pop())
ls = list.copy()
list2 = list+ls
print(list2)

