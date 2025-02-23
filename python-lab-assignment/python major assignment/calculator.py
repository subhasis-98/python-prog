print("\npress 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
print("press 5 for modulus ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

op = int(input("\nInput which type of operation you want to perform : "))

match(op):
    case 1: 
        print("Addition value = " , num1 + num2)
    case 2:
        print("Subtraction value = " , num1 - num2)
    case 3:
        print(" Multiplication value = " , num1 * num2)
    case 4:
        print("Division value = " , num1 / num2)        
    case 5:
        print("Modulus value = " , num1 % num2)
    case _:
        print("Invalid Input")
       