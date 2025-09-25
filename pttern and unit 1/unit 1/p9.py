#Gretest among three numbers.
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
if num1>num2 and num1>num3:
    print(f"Entered number {num1} is gretest.")
elif num2>num3:
    print(f"Entered number {num2} is gretest.")
else:
    print(f"Entered number {num3} is gretest.")
