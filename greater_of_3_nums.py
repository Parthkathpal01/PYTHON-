num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
if(num1 > num2 and num1 > num3):
    print("Number 1 is greater")
elif(num2 > num1 and num2 > num3):
    print("Number 2 is greater")
else:
    print("Number 3 is greater")