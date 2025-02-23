def max_frequency_char(s):
    max_char = ''
    max_count = 0
    for char in s:
        count = s.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char, max_count

print(max_frequency_char("hello"))
print(max_frequency_char("aabbcc"))
print(max_frequency_char("Python Rules")) 
print(max_frequency_char(""))
