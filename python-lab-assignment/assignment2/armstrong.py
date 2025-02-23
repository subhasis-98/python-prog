# Input: A 3-digit number
num = int(input("Enter a 3-digit number: "))
sq = len(str(num))
print(sq)
temp = num
sum = 0
while(num != 0):
    rem = num%10
    sum += rem**sq
    num //=10
if(temp == sum):
    print("armstrong")
else:
    print("not armstrong")