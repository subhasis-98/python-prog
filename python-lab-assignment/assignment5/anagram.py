def Anagram(str1, str2):
    match_count_str1 = 0
    match_count_str2 = 0
    spaces_in_str1 = 0
    spaces_in_str2 = 0
    
    # Count spaces in str1
    for char in str1:
        if char == ' ':
            spaces_in_str1 += 1
            
    # Count spaces in str2
    for char in str2:
        if char == ' ':
            spaces_in_str2 += 1

    # Check if characters in str1 match with their count in str2 (excluding spaces)
    for char in str1:
        if char in str2 and char != ' ':
            if str1.count(char) == str2.count(char):
                match_count_str1 += 1
                continue
            else:
                break
    
    # Check if characters in str2 match with their count in str1 (excluding spaces)
    for char in str2:
        if char in str1 and char != ' ':
            if str1.count(char) == str2.count(char):
                match_count_str2 += 1
                continue
            else:
                break

    # Return True if both strings are anagrams by excluding spaces
    return (match_count_str1 == len(str1) - spaces_in_str1 and match_count_str2 == len(str2) - spaces_in_str2)

# Test cases
str1 = 'william shakespeare'
str2 = 'i am a weakish speller'

print(Anagram(str1, str2))  # Should return True if they are anagrams
print(sorted(str1) == sorted(str2))  # Another method to check if the strings are anagrams
