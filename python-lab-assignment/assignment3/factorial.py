n = int(input("Enter a number = "))
total = 0
sign = 1
for i in range(1,2*n,2):
    # print(sign,end=" ")
    total += sign*i
    sign *= -1
print(total)