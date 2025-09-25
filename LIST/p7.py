#WAP to obtain a median value of a list of numnbers without disturbing the order of numbers in the list (already sorted)
import random
lst=[]
for i in range(11):
    lst.append(random.randint(1,100))
print("Unsorted =",lst)
s=sorted(lst)
print("Sorted =",s)
l=len(s)
if l%2==0:
    median=(s[l//2-1]+s[l//2])/2
else:
    median=s[l//2]
print(f"The median  of the  sorted list is:{median} ")