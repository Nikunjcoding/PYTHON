#suppose a list contain 20 integer generated random receve a number from keybord and report the position of all occurance of this number in the list.
import random
a=[]
i=1
while i<=20:
    num=random.randint(1,100)
    a.append(num)
    i+=1
print(a)
for index ,a in enumerate(a):
    print(index,end=" ")
    print(a)