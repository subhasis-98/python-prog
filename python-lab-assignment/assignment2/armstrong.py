# Input: A 3-digit number
num = int(input("Enter a 3-digit number: "))

# Check if the input is valid
if 100 <= num <= 999:
    # Extracting the digits of the number
    hundreds = num // 100  # Get the hundreds digit
    tens = (num // 10) % 10  # Get the tens digit
    units = num % 10  # Get the units digit

    # Calculate the sum of cubes of its digits
    armstrong_sum = (hundreds ** 3) + (tens ** 3) + (units ** 3)

    # Check if the number is an Armstrong number
    if num == armstrong_sum:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print("Please enter a valid 3-digit number.")
