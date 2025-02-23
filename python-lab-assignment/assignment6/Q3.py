sentence = input("Enter a sentence: ")
frequency = {}
for char in sentence.lower():
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
print("Letter Frequencies:")
for letter in frequency:
    print(letter, ":", frequency[letter])

