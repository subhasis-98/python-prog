def delete_char(s, i):
    if i < 0 or i >= len(s):  # Check if index is out of bounds
        return s  # Return the original string if index is invalid
    return s[:i] + s[i+1:]  # Concatenate parts before and after the index

# Test cases
s = "hello"
print(delete_char(s, 1))  # Output: "hllo"
print(delete_char(s, 0))  # Output: "ello"
print(delete_char(s, 4))  # Output: "hell"
print(delete_char(s, 5))  # Output: "hello" (index out of bounds)
