n = int(input("enter the number : "))
num = n
sum = 0
r =0
while(n>0):
    r = n%10
    sum += (r*r*r)
    n = n//10
if(num==sum):
    print("amstrong")
else:
    print("not amstrong")

