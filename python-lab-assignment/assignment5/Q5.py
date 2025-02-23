def are_anagrams(str1, str2):
    str11 = sorted(str1.replace(" ", "").lower())
    str22 = sorted(str2.replace(" ", "").lower())
    return str11 == str22
str1 = input()
str2 = input()
if are_anagrams(str1,str2):
    print("anagram")


  # False
