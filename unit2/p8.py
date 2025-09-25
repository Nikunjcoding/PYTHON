#finding factorial using function.
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Entr a number:"))
print(fact(n))