# Iterate over all numbers between 1 and 500
for num in range(1, 501):
    divisors_sum = 0
    # Find divisors of num (excluding the number itself)
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    # Check if the sum of divisors equals the number
    if divisors_sum == num:
        print(num)
