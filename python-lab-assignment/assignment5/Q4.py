greeting = 'hello students. How are you doing '

# Count the occurrences of a substring in the string.
print(greeting.count('you'))  # Output: 1

# Find the index of the first occurrence of a character.
print(greeting.find('s'))  # Output: 6

# Find the index of the last occurrence of a character.
print(greeting.rfind('s'))  # Output: 21

# Capitalize the first character and make the rest lowercase.
print(greeting.capitalize())  # Output: 'Hello students. how are you doing '

# Convert all characters to lowercase.
print(greeting.lower())  # Output: 'hello students. how are you doing '

# Convert all characters to uppercase.
print(greeting.upper())  # Output: 'HELLO STUDENTS. HOW ARE YOU DOING '

# Swap lowercase to uppercase and vice versa.
print(greeting.swapcase())  # Output: 'HELLO STUDENTS. hOW ARE YOU DOING '

# Check if the string follows title case (each word starts with uppercase).
print(greeting.istitle())  # Output: False

# Replace a substring with another substring.
print(greeting.replace('hello', 'hai'))  # Output: 'hai students. How are you doing '

# Remove leading and trailing spaces.
print(greeting.strip())  # Output: 'hello students. How are you doing'

# Split the string into a list of words.
print(greeting.split())  # Output: ['hello', 'students.', 'How', 'are', 'you', 'doing']

# Split into three parts: before the first match, the match, and after.
print(greeting.partition('.'))  # Output: ('hello students', '.', ' How are you doing ')

# Check if the string starts with a specific substring.
print(greeting.startswith('how'))  # Output: False

# Check if the string ends with a specific substring.
print(greeting.endswith('.'))  # Output: False
