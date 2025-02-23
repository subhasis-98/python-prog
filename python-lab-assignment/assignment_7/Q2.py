def count_words_and_vowels(file1):
    vowels = 'aeiouAEIOU'
    word_count = 0
    vowel_count = 0

    with open(file1, 'r') as file:
        for line in file:
            word_count += len(line.split())  # Count words
            vowel_count += sum(1 for char in line if char in vowels)  # Count vowels

    print(f"Number of words: {word_count}")
    print(f"Number of vowels: {vowel_count}")

# Example usage
count_words_and_vowels('datafile1.txt')
