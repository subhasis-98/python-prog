# Python program to convert a decimal number to binary

# Input from the user
n = int(input("Enter a number: "))
s = " "  # Initialize an empty string to store the binary representation

# Loop until the number becomes zero
while n != 0:
    r = n % 2  # Calculate the remainder (binary digit)
    n = n // 2  # Update n by dividing it by 2
    s = str(r) + s  # Add the remainder to the left side of the string

# Print the binary representation
print(s)
  
