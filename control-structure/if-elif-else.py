# greatest number among 3 number

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))

if(num1>num2 and num1>num3):
    print("First num is greater",num1)
elif(num2>num1 and num2>num3):
    print("Second num is greater",num2)
elif(num3>num1 and num3>num2):
    print("Third num is greater",num2)
else:
    print("all are equal")