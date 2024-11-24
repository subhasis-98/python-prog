# Input: Total amount of money
total_amount = int(input("Enter the total amount: "))

# Calculate the number of 20 rupee notes
notes_20 = total_amount // 20
remaining_amount = total_amount % 20

# Calculate the number of 10 rupee notes
notes_10 = remaining_amount // 10
remaining_amount %= 10

# Calculate the number of 5 rupee notes
notes_5 = remaining_amount // 5
remaining_amount %= 5

# Calculate the number of 1 rupee notes
notes_1 = remaining_amount

# Display the results
print(f"20 rupee notes: {notes_20}")
print(f"10 rupee notes: {notes_10}")
print(f"5 rupee notes: {notes_5}")
print(f"1 rupee notes: {notes_1}")
