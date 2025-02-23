def sin_approximation(x):
    result = 0 
    term = x
    n = 1
    while abs(term) > 1e-6:
        result += term 
        n += 2 
        term *= -x**2 / ((n - 1) * n)
    return result
