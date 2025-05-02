# Node class represents an element in the linked list-based stack
class StackNode:
    def __init__(self, data): 
        self.data = data       # Stores the data of the node
        self.next = None        # Pointer to the next node (initially None)

# Initialize the top of the stack as None (empty stack)
start = None

# Function to push an element onto the stack
def push(data):
    global start
    new_node = StackNode(data)  # Create a new node with the given data
    new_node.next = start    # Link the new node to the current top
    start = new_node         # Update the top to the new node

# Function to remove and return the top element from the stack
def pop():
    global start
    if start is None:  # If the stack is empty
        print("Stack is empty")
        return 
    popped_data = start.data  # Get the data from the top node
    start = start.next     # Move the top pointer to the next node
    return popped_data           # Return the popped data

# Function to return the top element without removing it
def peek():
    if start is None:  # If the stack is empty
        print("Stack is empty")
        return
    return start.data  # Return the data at the top of the stack

# Function to display all elements in the stack
def display_stack():
    if start is None:  # If the stack is empty
        print("Stack is empty")
        return
    current_node = start
    print("Stack elements:")
    while current_node:  # Traverse the stack from top to bottom
        print(current_node.data, end=" ")
        current_node = current_node.next  # Move to the next node
    print()  # Newline for clean output

# Menu-driven program to perform stack operations
while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display the top element")
    print("4. Display all stack elements")
    print("5. Quit")
    
    user_choice = int(input("Enter your choice: "))  # Get user's operation choice

    if user_choice == 1:
        data_to_push = int(input("Enter data to push: "))
        push(data_to_push)
    elif user_choice == 2:
        popped_data = pop()
        if popped_data is not None:
            print(f"Popped element: {popped_data}")
    elif user_choice == 3:
        top_data = peek()
        if top_data is not None:
            print(f"Top element: {top_data}")
    elif user_choice == 4:
        display_stack()
    elif user_choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
