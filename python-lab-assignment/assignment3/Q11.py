# Input: number of terms
n = int(input("Enter the number of terms (n >= 1): "))

a =0
b=1
print(a,b)
for i in range(2,n+1):
    next = a+b
    print(next,end=" ")
    a = b
    b = next
