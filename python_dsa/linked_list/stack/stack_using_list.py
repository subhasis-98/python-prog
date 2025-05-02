# Initialize the top pointer for the stack to -1, indicating an empty stack
top = -1

# Ask the user for the size of the stack
size = int(input("Enter size of the stack "))

# Function to push an item onto the stack
def push(stack, item):
    """
    Push an item onto the stack.
    
    :param stack: The stack in which the item will be pushed.
    :param item: The item to be pushed onto the stack.
    """
    global top
    # Check if the stack is full (overflow)
    if top >= size - 1:
        print("Overflow")  # Stack is full, cannot add more items
    else:
        top += 1  # Increment top to point to the next available position
        stack[top] = item  # Add the item to the stack

# Function to pop an item from the stack
def pop(stack):
    """
    Pop an item from the stack.
    
    :param stack: The stack from which the item will be popped.
    """
    global top
    # Check if the stack is empty (underflow)
    if top == -1:
        print('Underflow')  # No items to pop, stack is empty
    else:
        print("Popped item is:", stack[top])  # Display the popped item
        top -= 1  # Decrement top to remove the item

# Function to display the top item of the stack
def display_top(stack):
    """
    Display the top element of the stack.
    
    :param stack: The stack whose top element will be displayed.
    """
    global top
    # Check if the stack is empty
    if top == -1:
        print('Underflow')  # No items in the stack
    else:
        print("Top is:", stack[top])  # Display the top item

# Function to display all elements in the stack
def display(stack):
    """
    Display all elements of the stack from top to bottom.
    
    :param stack: The stack whose elements will be displayed.
    """
    global top
    # Check if the stack is empty
    if top == -1:
        print('Empty')  # No items to display
    else:
        print('Elements are:')
        # Display the elements from top to bottom
        for i in range(top, -1, -1):
            print(stack[i])  # Print each element

# Main menu for stack operations
stack = [0] * size
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display the top element")
    print("4. Display all stack elements")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = int(input("Enter the item to be pushed: "))
        push(stack, item)  # Call the push function
    elif choice == 2:
        pop(stack)  # Call the pop function
    elif choice == 3:
        display_top(stack)  # Call the display_top function
    elif choice == 4:
        display(stack)  # Call the display function
    elif choice == 5:
        break  # Exit the loop and quit the program
    else:
        print("Invalid choice. Try again.")  # Invalid input handling
