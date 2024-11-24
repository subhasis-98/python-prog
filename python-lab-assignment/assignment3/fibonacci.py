n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci Series:")
for i in range(1,n+1):
    print(a, end=" ")
    a, b = b, a + b
