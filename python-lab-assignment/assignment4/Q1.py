import math  # Importing the math module to access mathematical functions

# Using math.ceil() to return the smallest integer greater than or equal to the given number
print(math.ceil(65.65))  # Output: 66 (rounds up 65.65 to the next integer)
print(math.ceil(65.47))  # Output: 66 (rounds up 65.47 to the next integer)

# Using math.fabs() to return the absolute value of a number (always positive)
print(math.fabs(-67.58))  # Output: 67.58 (removes the negative sign)
print(math.fabs(3))       # Output: 3.0 (absolute value of 3 remains the same)

# Using math.exp() to calculate the exponential of a number (e^x, where e ≈ 2.71828)
print(math.exp(2.7))  # Output: 14.879731724872837 (calculates e^2.7)

# Using math.log() to calculate the logarithm of a number to a specified base
print(math.log(45, 2))  # Output: 5.491853096329675 (log base 2 of 45)

# Using math.log10() to calculate the logarithm of a number to base 10
print(math.log10(1000))  # Output: 3.0 (log base 10 of 1000 is 3, because 10^3 = 1000)

# Using math.pow() to raise a number to a power (x^y)
print(math.pow(4, 1/2))  # Output: 2.0 (calculates the square root of 4, because 4^(1/2) = 2)

# Using math.sqrt() to calculate the square root of a number
print(math.sqrt(121))  # Output: 11.0 (square root of 121 is 11)

# Using math.radians() to convert an angle from degrees to radians
print(math.radians(30))  # Output: 0.5235987755982988 (converts 30 degrees to radians)

# Using math.degrees() to convert an angle from radians to degrees
print(math.degrees(math.pi / 2))  # Output: 90.0 (converts π/2 radians to 90 degrees)
