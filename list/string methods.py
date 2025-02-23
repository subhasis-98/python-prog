original_text = "  Hello, Python is Awesome!  "

# 1. Convert the string to uppercase
uppercase_text = original_text.upper()
print("Uppercase:", uppercase_text)  # Output: "  HELLO, PYTHON IS AWESOME!  "

# 2. Convert the string to lowercase
lowercase_text = original_text.lower()
print("Lowercase:", lowercase_text)  # Output: "  hello, python is awesome!  "

# 3. Remove whitespace from the beginning and end
trimmed_text = original_text.strip()
print("Trimmed:", trimmed_text)  # Output: "Hello, Python is Awesome!"

# 4. Replace a word in the string
replaced_text = original_text.replace("Awesome", "Powerful")
print("Replaced:", replaced_text)  # Output: "  Hello, Python is Powerful!  "

# 5. Split the string into a list of words
words_list = original_text.split()  # Default split by spaces
print("Split into words:", words_list)  # Output: ['Hello,', 'Python', 'is', 'Awesome!']

# 6. Join the words list into a single string with a hyphen (-)
joined_text = "-".join(words_list)
print("Joined with hyphen:", joined_text)  # Output: "Hello,-Python-is-Awesome!"

# 7. Find the position of a word in the string
position = original_text.find("Python")
print("Position of 'Python':", position)  # Output: 9

# 8. Count occurrences of a specific letter
count_of_o = original_text.count("o")
print("Count of 'o':", count_of_o)  # Output: 3

# 9. Check if the string starts with "Hello"
starts_with_hello = original_text.strip().startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)  # Output: True

# 10. Check if the string ends with "Awesome!"
ends_with_awesome = original_text.strip().endswith("Awesome!")
print("Ends with 'Awesome!':", ends_with_awesome)  # Output: True
