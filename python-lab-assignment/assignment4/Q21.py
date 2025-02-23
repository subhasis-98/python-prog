def series_sum(x, n):
    total_sum = 0
    factorial = 1 
    for i in range(n):
        if i > 0:
            factorial *= (2 * i) * (2 * i - 1) 
        term = ((-1) ** i) * (x ** (2 * i)) / factorial
        total_sum += term
    return total_sum
