#patern 6.
num=int(input("enter the number of rows :"))
for i in range(1,num+1):
    for space in range(num-i):
        print(" ",end=" ")
    letter=65
    for j in range(1,i+1):
        print(chr(letter),end="   ")
        letter += 1
    print()