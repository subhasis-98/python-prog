data = [4, 5, 6, 7]

# Compute the sum of reciprocals
reciprocal_sum = 0
for i in data:
    reciprocal_sum += 1 / i

# Calculate the harmonic mean
harmonic_mean = len(data) / reciprocal_sum

# Print the result
print(f"T