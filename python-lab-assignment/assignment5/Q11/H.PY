def count_character_frequency(s):
    result = []
    for char in s:
        found = False
        for item in result:
            if item[0] == char:
                item[1] += 1
                found = True
                break
        if not found:
            result.append([char, 1])
    return result
print(count_character_frequency("hello"))   
print(count_character_frequency("aabbcc"))
print(count_character_frequency("Python Rules")) 