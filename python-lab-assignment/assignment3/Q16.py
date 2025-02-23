# Input: number of terms n
n = int(input("Enter a non-negative integer n: "))

# Initialize the sum of the series
series_sum = 0
factorial = 1

# Compute the sum of the first n factorials
for i in range(n + 1):
    if i > 0:
        factorial *= i  # Calculate factorial iteratively
    series_sum += factorial  # Add the factorial to the sum

# Print the result
print(f"The sum of the first {n} terms of the series is: {series_sum}")
