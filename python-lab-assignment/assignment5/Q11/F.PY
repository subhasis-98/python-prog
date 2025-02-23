def contains_digit_and_alpha(s):
    has_digit = False
    has_alpha = False
    for char in s:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_alpha = True
        if has_digit and has_alpha:
            return True
    return False

print(contains_digit_and_alpha("abc123"))  
print(contains_digit_and_alpha("12345"))   
print(contains_digit_and_alpha("abcde"))   
print(contains_digit_and_alpha("a1"))      
print(contains_digit_and_alpha(""))        
