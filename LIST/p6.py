#WAP to create  a list has 20 numbers.write a program thet removes all the duplicate from the list.
 
import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,100))
print(lst)
a=[]
for j in lst:
    if j not in a:
        a.append(j)
print(a)


