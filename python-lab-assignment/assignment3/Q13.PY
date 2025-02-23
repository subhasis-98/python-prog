# Input: positive integer n
n = int(input("Enter a positive integer: "))

# Reverse the digits
reversed_n = 0
while n > 0:
    digit = n % 10         # Get the last digit
    reversed_n = reversed_n * 10 + digit  # Append the digit to the reversed number
    n = n // 10            # Remove the last digit

# Print the reversed number
print("The reversed number is:", reversed_n)
