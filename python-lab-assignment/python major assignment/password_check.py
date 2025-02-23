# Password validation
password = input("Enter Password in string: ")
length = len(password)

if(length < 8):
    print("Error: Password must be at least 8")
else:
    upper = False
    for char in password:
        if char.isupper():
            upper = True
            break
    if not upper:
        print("Error: Password must contain at least one Capital letter")
    else:
        print("Password Created")
