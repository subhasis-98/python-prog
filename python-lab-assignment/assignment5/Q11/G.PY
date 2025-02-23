def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result

print(remove_duplicates("hello"))        
print(remove_duplicates("programming"))  
print(remove_duplicates("aabbcc"))       
print(remove_duplicates(""))            
