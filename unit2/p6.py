#sum of 3 number using function:
def sum(a,b,c):
    d=a+b+c
    return d
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:")) 
num3=int(input("Enter third number:"))
s=sum(num1,num2,num3)
print(f"sum of {num1},{num2} and {num3} is {s}")