# The abs() function returns the absolute value of a number.
print(abs(-5.4))  # Output: 5.4, since -5.4 becomes 5.4
print(abs(15))    # Output: 15, the absolute value of a positive number is the number itself

# The chr() function returns the string representing a character at the given Unicode code point.
print(chr(72))    # Output: 'H', since 72 corresponds to the character 'H' in Unicode

# The round() function rounds a floating-point number to the nearest integer.
print(round(-24.9))  # Output: -25, since -24.9 is rounded to the nearest integer, which is -25

# The float() function converts a number or string into a floating-point number.
print(float(57))     # Output: 57.0, converts the integer 57 to a floating-point number

# The complex() function returns a complex number with the specified real and imaginary parts.
print(complex(1+2j))  # Output: (1+2j), creates a complex number with real part 1 and imaginary part 2

# The divmod() function returns a tuple containing the quotient and the remainder when dividing two numbers.
print(divmod(5, 2))  # Output: (2, 1), quotient is 2, remainder is 1 when 5 is divided by 2

# Repeating float() to show conversion of integer to floating point again.
print(float(57))  # Output: 57.0, same as earlier conversion

# The pow() function returns the value of a number raised to a given power.
print(pow(9, 2))    # Output: 81, 9 raised to the power of 2 is 81

# The max() function returns the largest item from the provided arguments.
print(max(97, 88, 60))  # Output: 97, since 97 is the largest value

# The min() function returns the smallest item from the provided arguments.
print(min(55, 29, 99))  # Output: 29, since 29 is the smallest value

# The max() function can also be used with strings, returning the string that is considered largest.
print(max('a', 'b', 'AB'))  # Output: 'b', since 'b' comes after 'a' lexicographically and 'AB' is compared by the first letter, so 'b' is the largest
