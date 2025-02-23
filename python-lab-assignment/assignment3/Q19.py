# Input: integer n
n = int(input("Enter an integer: "))

# Initialize the sum of digits
sum_d = 0

# Loop to extract and sum the digits
while n > 0:
    sum_d += n % 10  # Add the last digit to the sum
    n = n // 10  # Remove the last digit

# Print the result
print("The sum of the digits is:", sum_d)
