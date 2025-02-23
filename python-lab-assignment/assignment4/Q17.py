def palindrome(num):
    temp = num
    rev = 0
    while(num>0):
        rem =  num%10
        rev = (rev*10 )+rem
        num //=10 
    if(rev == temp):
        print("is palindrome")
    else:    
        print("is not palindrome")

num = int(input("Enter the number to check : "))
palindrome(num)