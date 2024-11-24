
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))

if(num1>num2 and num1>num3):
    print("first ",num1,"is the greatest number")
elif(num2>num3):
    print("second ",num2,"is the greatest number")
else:
    print("third ",num3,"is the greatest number")
    