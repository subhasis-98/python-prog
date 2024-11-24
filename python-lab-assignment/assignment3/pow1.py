n = int(input("Enter the value of n = "))
x = int(input("Enter the value of x = "))

fact = 1
for i in range(1,n+1):
    fact*=i
# print("",fact)
print()

pow1 = x**n /fact

print("x**n/n! = ",pow1)
