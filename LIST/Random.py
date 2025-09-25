#create random list using while loop.
import random
a=[]
i=1
while i<=20:
    num=random.randint(1,100)
    a.append(num)
    i+=1
print(a)
#create random list using for loop.
import random
b=[]
for i in range(20):
    b.append(random.randint(1,100))
print(b)
