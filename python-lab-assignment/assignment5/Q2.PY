# 2. Write a function that takes a string as a parameter and returns a string with every successive repetitive 
# character replaced with a star(*). For example, ‘hello’ is returned as ‘he**o’. 

def replace_repeats_with_star(s):
    result = " "
    for i in range(len(s)):
        # Check if it's the first character or different from the previous one
        if i > 0 and s[i] == s[i - 1]:
            result += "*"
        else:
            result += s[i]
    return result


# Input from the user
input_string = input("Enter a string: ")

# Get the result and print it
output = replace_repeats_with_star(input_string)
print("Modified string:", output)

