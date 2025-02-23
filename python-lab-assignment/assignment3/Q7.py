# num = int(input("Enter a number : "))
# sum =0
# for i in range (1,num+1):
#     sum += (1/i )
# print(sum)

# List of numbers
data = [4, 5, 6, 7]

# Compute the sum of reciprocals
reciprocal_sum = 0
for i in data:
    reciprocal_sum += 1 / i

# Calculate the harmonic mean
harmonic_mean = len(data) / reciprocal_sum

# Print the result
print(f"The harmonic mean of {data} is {harmonic_mean:.2f}")
