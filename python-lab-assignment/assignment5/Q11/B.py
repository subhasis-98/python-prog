def pallindrome(str):
    str1 = str[::-1]
    return str == str1
str = input("Enter string :")
print(pallindrome(str))