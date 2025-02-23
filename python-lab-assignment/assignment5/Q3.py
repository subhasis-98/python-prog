address = "Plot-6, Nayapalli, Bhubaneswar "

# Calculate the length of the string (total number of characters, including spaces and punctuation).
print(len(address))  # Output: 32

# Slice the string to extract characters starting at index 17 up to the second-to-last character.
print("\n", address[17:-1])  # Output: " Bhubaneswar"

# Slice the string from the first character to the last using its length dynamically.
print("\n", address[-len(address): len(address)])  # Output: "Plot-6, Nayapalli, Bhubaneswar "

# Concatenate the first two characters of the string with the last 11 characters.
print("\n", address[:2] + address[-11:])  # Output: "Plhubaneswar "

# Find the index of the first occurrence of the substring "bhubaneswar".
# Case-sensitive, so it won't find "Bhubaneswar" (output will be -1 if not found).
print("\n", address.find("bhubaneswar"))  # Output: -1

# Swap the case of each character in the string (lowercase becomes uppercase and vice versa).
print("\n", address.swapcase())  # Output: "pLOT-6, nAYAPALLI, bHUBANESWAR "

# Split the string into a list using "," as the delimiter.
print("\n", address.split(","))  # Output: ['Plot-6', ' Nayapalli', ' Bhubaneswar ']

# Check if all characters in the string are alphabetic (returns False due to numbers, spaces, and punctuation).
print("\n", address.isalpha())  # Output: False
