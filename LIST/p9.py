# A list contain only +ve and -ve integers . WAP to obtain the numbers of -ve numbers in the list.
import random
lst=[]
for i in range(20):
    lst.append(random.randint(-20,20))
print(lst)
count=0 
for i in lst:
    if i<0:
        count+=1
        #print("The number of -ve integers in the list is:",i)
print("The total number of -ve integers in the list is:",count)
