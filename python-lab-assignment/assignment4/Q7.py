def sum_even_digits(num):
    digits = str(num)
    sum_of_evens = 0
    
    if int(digits[0]) % 2 == 0:
        sum_of_evens += int(digits[0])
    if int(digits[1]) % 2 == 0:
        sum_of_evens += int(digits[1])
    if int(digits[2]) % 2 == 0:
        sum_of_evens += int(digits[2])
    if int(digits[3]) % 2 == 0:
        sum_of_evens += int(digits[3])
    return sum_of_evens
result = sum_even_digits(2468)
print("Sum of even digits:", result)
