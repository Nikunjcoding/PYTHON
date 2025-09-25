#check number is -ve ,+ve or zero.
num=int(input("Enter the number:"))
if num>0:
    print(f"Entered number {num} is positive.")
elif num<0:
    print(f"Entered number {num} is negative")
else:
    print(f"Entered number {num} is zero")