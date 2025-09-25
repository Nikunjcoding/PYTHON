#product and average of 5 number using function:
def mul_avg(a,b,c,d,e):
    mul=a*b*c*d*e
    avg=(a+b+c+d+e)/5
    return mul,avg
a=int(input("Enter first number:"))  
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
e=int(input("Enter  5th number:"))
f,g=mul_avg(a,b,c,d,e)
print(f,g)