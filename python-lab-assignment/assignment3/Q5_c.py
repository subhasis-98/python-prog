for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print(" ", end=" ")
    # Print stars
    for k in range(1, 2 * i):  # This ensures stars increase as 1, 3, 5, 7, 9
        print("*", end=" ")
    # Move to the next line
    print()
