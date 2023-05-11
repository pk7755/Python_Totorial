for letter in 'Python':
    print(letter)


fruits = ['apple','banana','mango']
for x in fruits:
    print(x)

for index in range(len(fruits)):
    print ('current fruits :',(fruits[index]))

print('===========================================================')
i=0
for num in range(i,100):     #to iterate between 10 to 20
   for i in range(2,(num//2+1)):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
        #  j=num/i             #to calculate the second factor
        #  print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
     print (num, 'is a prime number')
     i=i+1
     