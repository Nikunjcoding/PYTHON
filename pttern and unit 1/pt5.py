#patern 1.
num=int(input("enter the number of rows :"))
for i in range(1,num+1):
    for space in range(num-i):
        print(" ",end=" ")
    for star in range(i):
        print("*",end="   ")
    print()