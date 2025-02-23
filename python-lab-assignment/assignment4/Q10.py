def UpperCase(char):
    
        uppercase_char = chr(ord(char) - 32)
        return uppercase_char
user_input = input("Enter a lowercase alphabet (a-z): ")
result = UpperCase(user_input)
print("Converted to uppercase:", result)
