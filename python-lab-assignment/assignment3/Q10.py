# n = int(input("Enter the value of n = "))
# x = int(input("Enter the value of x = "))
# POWER=1
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# # print("",fact)
# print()
# POWER = x**n
# pow1 = POWER /fact

# print("x**n/n! = ",pow1)


# Input: values of x and n
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n (n >= 0): "))

# Initialize factorial and power result
factorial = 1
power = 1

# Compute n! (factorial)
for i in range(1, n + 1):
    factorial *= i

# Compute x^n
power = x ** n

# Compute the result x^n / n!
result = power / factorial

# Print the result
# print(f"The value of x^{n} / {n}! is: {result:.6f}")
print("x**n/n! = ",result)
