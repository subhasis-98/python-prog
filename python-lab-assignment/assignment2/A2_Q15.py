# Input: Total amount of money
total  = int(input("Enter the total amount: "))

# Calculate the number of 20 rupee notes
notes20 = total // 20
rem = total%10

notes10 = rem //10
rem %= 10

notes5 = rem//5
rem %= 5

notes1 = rem

# print()
print(notes20)
print(notes10)
print(notes5)
print(notes1)