

def xyz(ls):
    odd = 0
    even = 0
    for i in ls:
        if i%2==0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [2,334,4,556,5,6,76,7,67,54]
even,odd = xyz(lst)
print("Odd no in the list is : ",odd)
print("Even no in the list is : ",even)