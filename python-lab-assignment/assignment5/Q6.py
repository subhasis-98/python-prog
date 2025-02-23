str = input("Enter String : ")
lower = str.lower()
words = lower.split()
count = 0
for char in words:
    print(char)
    if char[0] == 'a' or char[0] == 'e' or char[0] == 'i' or char[0] == 'o' == char[0] == 'u':
        count += 1
print("Count Vowel is : ",count)

