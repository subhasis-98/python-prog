num = int(input("Enter the number between 100 and 999 : "))

sum = 0
# temp =num
while(num>0):
    rem = num%10
    num = num//10
    sum += rem
print(sum)
