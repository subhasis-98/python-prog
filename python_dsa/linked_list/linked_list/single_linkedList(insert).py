# SINGLE LINKED LIST (INSERTION ONLY VERSION)

# Node class represents an individual element (node) in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the data value in this node
        self.next = None      # Initialize next pointer to None (points to no next node yet)

# Global pointers to track the start and end of the linked list
start = end = None

# Function to insert a new node at the beginning of the list
def insert_at_beginning(data):
    global start, end
    new_node = Node(data)            # Create a new node with the given data
    if start is None:                # If the list is currently empty
        start = end = new_node       # Start and end both point to the new node
    else:
        new_node.next = start        # New node points to the current start node
        start = new_node             # Update start to the new node

# Function to insert a new node at the end of the list
def insert_at_end(data):
    global start, end
    new_node = Node(data)            # Create a new node with the given data
    if start is None:                # If the list is empty
        start = end = new_node       # Both start and end point to this node
    else:
        end.next = new_node          # Last node's next points to the new node
        end = new_node               # Update end to point to the new node

# Function to insert a new node at a specific position (1-based index)
def insert_at_position(pos, data):
    global start, end
    
    # If position is 1, insert the node at the beginning
    if pos == 1:
        insert_at_beginning(data)  # Call the insert_at_beginning function to insert at the start of the list
        return
    
    # Check if the position is valid (greater than 0 and less than or equal to the number of nodes in the list + 1)
    if pos > count_nodes() + 1 or pos < 1:
        print("Out of Bounds")  # Print error message if the position is invalid
        return
    
    new_node = Node(data)  # Create a new node with the given data
    
    # Initialize two pointers: `curr` for current node and `prev` for the previous node
    curr, prev = start, None
    i = 1  # Start counting from position 1
    
    # Traverse the list until we reach the desired position or the end
    while curr is not None and i < pos:

        prev = curr  # Move `prev` to the current node
        curr = curr.next  # Move `curr` to the next node
        i += 1  # Increment the position counter
    
    prev.next = new_node  # Link the previous node to the new node
    new_node.next = curr  # Link the new node to the current node
    
    # If the current node is None, we inserted at the end, so we update the `end` pointer
    if curr is None:
        end = new_node      # Update the end pointer if the new node is inserted at the end of the list


# Function to insert a new node before a specific element
def insert_before_element(elem, data):
    global start, end
    new_node = Node(data)   # Create a new node with the given data
    if start is None:  # Check if the list is empty (start is None)
        print("Empty")  # If the list is empty, print a message
        return  # Exit the function since no insertion can happen in an empty list
    if start.data == elem:    # If the element to insert before is the first node (start)
        insert_at_beginning(data)  # Call the function to insert the node at the beginning
        return  # Exit the function after inserting at the beginning
    # Initialize pointers to traverse the list
    curr, prev = start, None  # 'curr' will point to the current node, 'prev' will point to the previous node
    # Traverse the list to find the element before which to insert the new node
    while curr and curr.data != elem:
        prev = curr  # Move the 'prev' pointer to the current node
        curr = curr.next  # Move the 'curr' pointer to the next node in the list
    # If the element was not found in the list, print a message and return
    if curr is None:
        print(f"Element {elem} not found in list")  # If the element is not found, print an error message
        return  # Exit the function
    # If the element is found, we insert the new node before it
    prev.next = new_node  # Point the previous node's 'next' to the new node (this inserts the new node)
    new_node.next = curr  # Point the new node's 'next' to the current node (this keeps the list connected)


# Function to insert a new node after a specific element
def insert_after_element(elem, data):
    global start, end  # Access the global start and end pointers of the linked list
    new_node = Node(data)  # Create a new node with the given data
    if start is None:  # Check if the list is empty
        print("Empty")  # If empty, print "Empty" and return
        return  # Exit the function since we can't insert in an empty list
    curr = start  # Initialize the current node pointer to the start of the list
    while curr and curr.data != elem:  # Traverse the list to find the element `elem`
        curr = curr.next  # Move to the next node in the list
    if curr is None:  # If the element was not found in the list (i.e., end of list is reached)
        print("Not found")  # Print "Not found" to inform the user
        return  # Exit the function as the element was not found, so we can't insert
    new_node.next = curr.next  # Link the new node's next pointer to the current node's next node
    curr.next = new_node  # Link the current node's next pointer to the new node, inserting it after
    if curr == end:  # Check if the current node is the last node in the list
        end = new_node  # If it is, update the end pointer to point to the new node (new last node)


# Function to count the number of nodes in the list
def count_nodes():
    curr, count = start, 0
    while curr:
        count += 1
        curr = curr.next
    return count

def found(data):
    global start, end  
    curr = start
    while curr is not None:
        if curr.data == data:
            print(f"data found {curr.data}")
            return
        curr = curr.next
    print("data not found")

# Function to display the elements of the list
def display():
    curr = start
    if curr is None:
        print("List is Empty")
        return
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Menu-driven interface
while True:
    print("\n------ SINGLE LINKED LIST MENU ------")
    print("1> Insert at beginning")
    print("2> Insert at end")
    print("3> Insert at a specific position")
    print("4> Count total nodes")
    print("5> Insert before an element")
    print("6> Insert after an element")
    print("7> Display list")
    print("8> Exit")
    print("9> Search an element")  # ✅ Now properly shown to the user

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert at beginning: "))
        insert_at_beginning(value)
    elif choice == 2:
        value = int(input("Enter value to insert at end: "))
        insert_at_end(value)
    elif choice == 3:
        pos = int(input("Enter position: "))
        value = int(input("Enter value: "))
        insert_at_position(pos, value)
    elif choice == 4:
        print("Total number of nodes:", count_nodes())
    elif choice == 5:
        target = int(input("Enter element before which to insert: "))
        value = int(input("Enter value to insert: "))
        insert_before_element(target, value)
    elif choice == 6:
        target = int(input("Enter element after which to insert: "))
        value = int(input("Enter value to insert: "))
        insert_after_element(target, value)
    elif choice == 7:
        display()
    elif choice == 8:
        print("Exiting program...")
        break
    elif choice == 9:
        value = int(input("Enter value to search: "))
        found(value)  # ✅ Fixed: removed `break` so the program doesn't exit after search
    else:
        print("Invalid choice, please try again.")
