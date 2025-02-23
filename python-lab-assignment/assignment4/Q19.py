def palindrome(num,num1):
    temp = num
    rev = 0
    while(num>0):
        rem =  num%10
        rev = (rev*10 )+rem
        num //=10 
    if(rev == num1):
        print(f"{temp} and {num1} are co-palindrome")
    else:    
        print(f"{temp} and {num1} are not co-palindrome")
        # print(f"The factorial of {number} is: {factorial(number)}")

num = int(input("Enter the first number to check : "))
num1 = int(input("Enter the second number to check : "))

palindrome(num,num1)