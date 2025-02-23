def string_length(s):
    length = 0
    for _ in s:
        length += 1
    return length

print(string_length("hello"))       
print(string_length("Python"))      
print(string_length(""))            
print(string_length("12345 67890"))  
