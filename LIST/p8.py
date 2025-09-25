#suppose a list contain several words write a program that create an other list that contain the 1st charactor of each word in the first list.
import random
lst=[]
for i in range(5):
    l=input("Enter the words:")
    lst.append(l)
#print(lst)
a=[]
for j in lst:
    a.append(j[0])
print(a)
