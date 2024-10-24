num = int(input("Enter the number = "))
if(num%2 == 0):
    print("number is even")
    if(num%4 == 0 and num%8 == 0):
        print("number is even and divisible by 4 and 8")
    else:
        print("number is even and not divisible by 4 and 8")
else:
    print("number is odd")
    if(num%3 == 0 and num%7 == 0):
         print("number is odd and divisible by 3 and 7")
    else:
         print("number is odd and not divisible by 3 and 7")
        
            