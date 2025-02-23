# n = int(input("Enter a number = "))
# total = 0
# sign = 1
# for i in range(1,2*n,2):
#     # print(sign,end=" ")
#     total += sign*i
#     sign *= -1
# print(total)

# Input: number of terms
n = int(input("Enter the number of terms (n >= 1): "))

# Initialize the sum
S = 0

# Compute the sum of the series
for i in range(1, n + 1):
    if i % 2 == 1:  # Odd term (add)
        S += (2 * i - 1)
    else:           # Even term (subtract)
        S -= (2 * i - 1)

# Print the result
print(f"The sum of the first {n} terms of the series is: {S}")

