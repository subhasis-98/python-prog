class Node:
    def __init__(self, data):  # Constructor to initialize a node
        self.data = data  # Store the value of the node
        self.next = None  # Pointer to the next node (initially None)
        self.prev = None  # Pointer to the previous node (initially None)

# Global variable to keep track of the start of the linked list
start = end=None

def insert_at_beginning(value):
    """Insert a new node at the beginning of the doubly linked list."""
    global start,end
    new_node = Node(value)  # Create a new node
    if start is None:
        start =end= new_node  # If list is empty, make new node the start
    else:
        start.prev = new_node  # Link current start to new node
        new_node.next = start  # Set new node's next to current start
        start = new_node  # Update start to new node

def insert_at_end(value):
    """Insert a new node at the end of the doubly linked list."""
    global start,end
    new_node = Node(value)  # Create a new node
    if start is None:
        start =end= new_node  # If list is empty, set new node as start
    else:
        current = start
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Link last node to new node
        new_node.prev = current  # Link new node to last node
        end = new_node  # Update end to the new last node

def count_nodes():
    """Count the number of nodes in the doubly linked list."""
    current, count = start, 0
    while current:  # Traverse the list and count nodes
        current, count = current.next, count + 1
    return count

def insert_at_position(position, value):
    """Insert a new node at a specific position."""
    global start,end
    if position > count_nodes() + 1:
        print("Insertion not possible: Position out of range")
        return
    elif position == 1:
        insert_at_beginning(value)
        return
    
    current = start
    i = 1
    while i < position - 1 and current:
        current = current.next
        i += 1

    new_node = Node(value)
    new_node.next = current.next  # Link new node to next node
    if current.next:
        current.next.prev = new_node
    current.next = new_node  # Link previous node to new node
    new_node.prev = current
    


def insert_before_element(target_value, value):
    """Insert a new node before a given element."""
    global start  # Use the global start pointer to access the beginning of the list
    
    current = start  # Start traversing from the beginning of the list

    # Traverse the list to find the node with the target_value
    while current and current.data != target_value:  
        current = current.next  # Move to the next node

    # If we reach the end and didn't find the element
    if not current:   #if current is None
        print("Element not found!")  # Print error if target not found
        return  # Exit the function

    # Create a new node with the given value
    new_node = Node(value)
    # Link the new node to point to the current node (node with target_value)
    new_node.next = current
    # Link the new node’s prev to the previous node of current
    new_node.prev = current.prev

    # If the current node is not the first node
    if current.prev:
        current.prev.next = new_node  # Connect the previous node to the new node
    else:
        start = new_node  # If inserting before the first node, update start
    # Finally, update the current node's prev to point back to the new node
    current.prev = new_node

def insert_after_element(target_value, value):
    """Insert a new node after a given element."""
    global start ,end # Access the global start pointer of the doubly linked list
    current = start  # Start from the beginning of the list
    # Traverse the list to find the node with data equal to target_value
    while current and current.data != target_value:
        current = current.next
    # If target_value is not found in the list
    if not current:
        print("Element not found!")
        return  # Exit the function

    new_node = Node(value)  # Create a new node with the given value
    new_node.next = current.next  # Point new_node's next to the node after current
    new_node.prev = current  # Point new_node's prev to the current node (we're inserting after it)

    # If current is not the last node, update the next node's prev to point to the new node
    if current.next:
        current.next.prev = new_node # Update next node's prev to new_node
    else:
        end = new_node  # If inserting at the end, update the global end pointer

    current.next = new_node  # Link the current node's next to the new node


def display():
    """Display the elements of the doubly linked list."""
    current = start
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

def search_element(value):
    """Search for an element in the list and return its position."""
    current, position = start, 1
    while current:
        if current.data == value:
            return position
        current, position = current.next, position + 1
    return -1  # Return -1 if not found

# Menu-driven interface for user interaction
while True:
    print("\nDoubly Linked List Operations:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Insert Before Element")
    print("5. Insert After Element")
    print("6. Search for Element")
    print("7. Display List")
    print("8. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        insert_at_beginning(value)
    elif choice == 2:
        value = int(input("Enter value to insert: "))
        insert_at_end(value)
    elif choice == 3:
        position = int(input("Enter position: "))
        value = int(input("Enter value to insert: "))
        insert_at_position(position, value)
    elif choice == 4:
        target = int(input("Enter element before which to insert: "))
        if search_element(target) != -1:
            value = int(input("Enter value to insert: "))
            insert_before_element(target, value)
        else:
            print("Element not found!")
    elif choice == 5:
        target = int(input("Enter element after which to insert: "))
        value = int(input("Enter value to insert: "))
        insert_after_element(target, value)
    elif choice == 6:
        target = int(input("Enter element to search: "))
        position = search_element(target)
        if position != -1:
            print(f"Element {target} found at position {position}")
        else:
            print(f"Element {target} not found")
    elif choice == 7:
        display()
    elif choice == 8:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
