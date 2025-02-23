
# Display menu options
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exit")
   
    # Get the user's choice

while True:
    option = int(input("\nEnter your option: "))
    # Handle exit option
    if option == 6:
        print("Exiting the program. Goodbye!")
        break
    
    # Check if the option is valid
    if (option ==1 or option == 2 or option==3 or option==4 or  option == 5 ):
        # Get input numbers
        n1 = int(input("Enter number n1: "))
        n2 = int(input("Enter number n2: "))
        
        # Perform the chosen operation
        if option == 1:
            print("Addition result is:", n1 + n2)
        elif option == 2:
            print("Subtraction result is:", n1 - n2)
        elif option == 3:
            print("Multiplication result is:", n1 * n2)
        elif option == 4:
            if n2 != 0:  # Avoid division by zero
                print("Division result is:", n1 / n2)
            else:
                print("Error: Division by zero is not allowed.")
        elif option == 5:
            if n2 != 0:  # Avoid modulo by zero
                print("Modulo result is:", n1 % n2)
            else:
                print("Error: Modulo by zero is not allowed.")
        # elif option == 6:
        #     print("Modulo result is:", n1 % n2)

    else:
        print("Invalid option. Please try again.")


