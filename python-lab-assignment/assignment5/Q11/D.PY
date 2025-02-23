def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


print(count_vowels_consonants("hello"))          
print(count_vowels_consonants("Python Rules!"))  
print(count_vowels_consonants("12345"))          
print(count_vowels_consonants(""))               
