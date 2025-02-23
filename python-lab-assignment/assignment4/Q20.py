def sum_prod():
    num1 = int(input("Enter Num1 : "))
    num2 = int(input("Enter Num2 : "))
    sum = 0
    for i in range (1,num2+1):
        sum += num1
    print("Multiply is :",sum)
    print("prod is :",num1*num2)
sum_prod()
