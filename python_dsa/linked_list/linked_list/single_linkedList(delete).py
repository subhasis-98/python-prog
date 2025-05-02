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



# delete functions 
# Function to delete a node from the beginning of the list
def delete_from_beginning():
    global start, end  # Access global pointers
    
    if start is None:  # Check if the list is empty
        print("List is empty")  # Message for user
        return  # No deletion possible

    print(f"Deleted: {start.data}")  # Display the value being deleted
    start = start.next  # Move the start pointer to the second node (skip the first node)
    if start is None:  # If the list becomes empty after deletion
        end = None  # Set end to None as well

# Function to delete a node from the end of the list
def delete_from_end():
    global start, end  # Access global pointers
    if start is None:  # If list is empty
        print("List is empty")  # Inform the user
        return
    if start == end:  # If the list has only one node
        print(f"Deleted: {start.data}")  # Display the node value
        start = end = None  # Empty the list
        return
    curr = start  # Start traversal from the first node
    # Traverse the list until the second-last node (node before 'end')
    while curr.next != end:
        curr = curr.next

    print(f"Deleted: {end.data}")  # Display the value to be deleted

    curr.next = None  # Remove the last node by disconnecting it
    end = curr  # Update end pointer to new last node

# Function to delete a node at a specific position (1-based index)
def delete_at_position(pos):
    global start, end

    # Case 1: If list is empty
    if start is None:
        print("List is empty")
        return

    # Case 2: Invalid position
    if pos < 1 or pos > count_nodes():
        print("Invalid position")
        return

    # Case 3: Deleting the first node
    if pos == 1:
        delete_from_beginning()
        return

    # Case 4: Deleting a node at position > 1
    curr, prev = start, None
    i = 1  # Position counter

    # Traverse to the desired position
    while curr and i < pos:
        prev = curr
        curr = curr.next
        i += 1

    # Now 'curr' points to the node to delete
    prev.next = curr.next  # Remove the node by skipping it

    if curr == end:
        end = prev  # If last node is deleted, update end

    print(f"Deleted: {curr.data}")  # Show the deleted value



# Function to delete a node by its value
def delete_by_value(value):
    global start, end  # Access the global pointers 'start' and 'end' used to track the list

    if start is None:  # Check if the list is empty
        print("List is empty")  # Inform the user that deletion can't happen
        return  # Exit the function early

    if start.data == value:  # If the value to delete is in the first node
        delete_from_beginning()  # Use existing function to delete the first node
        return  # Exit after deletion

    curr = start  # 'curr' will traverse the list starting from the first node
    prev = None   # 'prev' will follow one step behind 'curr' to keep track of the previous node

    # Traverse the list to find the node with the matching value
    while curr and curr.data != value:  # Continue as long as the value doesn't match and list hasn't ended
        prev = curr  # Move 'prev' to current node
        curr = curr.next  # Move 'curr' to the next node

    if curr is None:  # If we reach the end of the list and value wasn't found
        print("Value not found")  # Inform the user
        return  # Exit without making any changes

    # If value is found, delete the node by linking previous node to current's next node
    prev.next = curr.next  # This bypasses the node with matching value (removes it from the chain)

    if curr == end:  # If the deleted node was the last node
        end = prev  # Update the 'end' pointer to point to the new last node

    print(f"Deleted: {curr.data}")  # Print the deleted node's value for confirmation

    curr, prev = start, None  # Reinitialize 'curr' and 'prev' to default (not necessary here, can be removed)



# Function to count the number of nodes in the list
def count_nodes():
    curr, count = start, 0
    while curr:
        count += 1
        curr = curr.next
    return count

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
# Menu-driven program to use the linked list operations

def menu():
    while True:
        print("\n--- Linked List Operations Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Insert Before Element")
        print("5. Insert After Element")

        print("6. Delete from Beginning")
        print("7. Delete from End")
        print("8. Delete at Position")
        print("9. Delete by Value")
        print("10. Count Nodes")
        print("11. Display List")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        match choice:
            case '1':
                data = int(input("Enter data to insert at beginning: "))
                insert_at_beginning(data)
            case '2':
                data = int(input("Enter data to insert at end: "))
                insert_at_end(data)
            case '3':
                pos = int(input("Enter position to insert at: "))
                data = int(input("Enter data to insert: "))
                insert_at_position(pos, data)
            case '4':
                elem = int(input("Enter the element before which to insert: "))
                data = int(input("Enter data to insert: "))
                insert_before_element(elem, data)
            case '5':
                elem = int(input("Enter the element after which to insert: "))
                data = int(input("Enter data to insert: "))
                insert_after_element(elem, data)
            case '6':
                delete_from_beginning()
            case '7':
                delete_from_end()
            case '8':
                pos = int(input("Enter position to delete: "))
                delete_at_position(pos)
            case '9':
                value = int(input("Enter value to delete: "))
                delete_by_value(value)
            case '10':
                total = count_nodes()
                print(f"Total nodes in the list: {total}")
            case '11':
                display()
            case '12':
                print("Exiting program.")
                exit()  # or use break inside a while loop
            case _:
                print("Invalid choice. Please enter a number between 1 and 12.")
# Run the menu
menu()
