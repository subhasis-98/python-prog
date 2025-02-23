def swap_values(a, b):
    # a, b = b, a
    c=a
    a=b
    b=c
    return a, b

x = 5
y = 10

print("Before swapping:")
print("x =", x)
print("y =", y)

x, y = swap_values(x, y)

print("\nAfter swapping:")
print("x =", x)
print("y =", y)
