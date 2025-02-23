# Input: value of x and number of terms n
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms n: "))

# Initialize the sum of the series
series_sum = 0
factorial = 1

# Compute the sum of the first n terms of the series
for i in range(1, n + 1):
    factorial *= i  # Compute factorial iteratively
    series_sum += (x ** i) / factorial  # Add the current term to the sum

# Print the result
print("The sum of the series is:", series_sum)
