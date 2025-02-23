# Input: value of x and number of terms n
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))

# Initialize the sum of the series
series_sum = 0
sign = 1  # To alternate the sign for each term
factorial = 1

# Compute the sum of the first n terms of the series
for i in range(1, 2*n, 2):  # Iterating over the powers of x (1, 3, 5, 7, ...)
    if i > 1:
        factorial *= i * (i - 1)  # Compute the factorial for odd numbers (3!, 5!, 7!, etc.)
    series_sum += sign * (x ** i) / factorial  # Add or subtract the current term
    sign *= -1  # Alternate the sign for the next term

# Print the result
print("The sum of the series is:", series_sum)
