input_string = input("Enter String : ")
s = ""
for char in input_string:
    print("char :",char)
    s = char + s
    print("s = ",s)
print(s)