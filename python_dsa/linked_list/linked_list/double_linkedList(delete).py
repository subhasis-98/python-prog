# Define the Node class for the doubly linked list
class Node:
    def __init__(self, data):
        """
        Initialize a new node with data and pointers to next and previous nodes.
        
        :param data: Value to be stored in the node.
        """
        self.data = data       # Stores data in the node
        self.next = None       # Pointer to the next node
        self.previous = None   # Pointer to the previous node

# Global pointers to keep track of the start and end of the list
start = end = None

# Function to insert a node at the beginning of the list
def insert_at_beginning(value):
    """
    Insert a new node at the beginning of the doubly linked list.
    
    :param value: The value to be inserted at the beginning.
    """
    global start, end
    new_node = Node(value)  # Create new node
    if start is None:       # If list is empty
        start = end = new_node
    else:
        new_node.next = start  # Link new node to old start
        start.previous = new_node  # Link old start back to new node
        start = new_node       # Update start to new node

# Function to insert a node at the end of the list
def insert_at_end(value):
    """
    Insert a new node at the end of the doubly linked list.
    
    :param value: The value to be inserted at the end.
    """
    global start, end
    new_node = Node(value)
    if start is None:       # If list is empty
        start = end = new_node
    else:
        end.next = new_node    # Link current end to new node
        new_node.previous = end    # Link new node back to old end
        end = new_node         # Update end to new node

# Function to insert a node at a specific position
def insert_at_position(position, value):
    """
    Insert a new node at a specific position in the doubly linked list.
    
    :param position: The position at which the node needs to be inserted.
    :param value: The value to be inserted at the given position.
    """
    global start, end  # Access the global pointers 'start' and 'end' of the list

    # Check if the given position is beyond the allowed range (1 to count_nodes + 1)
    if position > count_nodes() + 1:
        print("Insertion not possible: Position out of range")
        return

    # If position is 1, delegate to insert_at_beginning() function
    elif position == 1:
        insert_at_beginning(value)
        return

    # Start from the beginning of the list
    current = start
    i = 1  # Position tracker starting at 1
    # Traverse the list until we reach the node just before the desired position
    while i < position - 1 and current:
        current = current.next
        i += 1

    # Create a new node with the given value
    new_node = Node(value)
    # Point the new node's next to the node currently after 'current'
    new_node.next = current.next

    # If there is a node after 'current', update its previous pointer to the new node
    if current.next:
        current.next.previous = new_node

    # Link 'current' node's next to the new node (placing new node after current)
    current.next = new_node
    # Point new node's previous to the 'current' node (placing new node before its next node)
    new_node.previous = current

# Function to insert a node before a given element
def insert_before_element(target_value, value):
    """
    Insert a new node before a node containing a given value.
    
    :param target_value: The value of the node before which the new node will be inserted.
    :param value: The value to be inserted.
    """
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
    # Link the new node’s previous to the previous node of current
    new_node.previous = current.previous

    # If the current node is not the first node
    if current.previous:
        current.previous.next = new_node  # Connect the previous node to the new node
    else:
        start = new_node  # If inserting before the first node, update start
    # Finally, update the current node's previous to point back to the new node
    current.previous = new_node

# Function to insert a node after a given element
def insert_after_element(target_value, value):
    """
    Insert a new node after a node containing a given value.
    
    :param target_value: The value of the node after which the new node will be inserted.
    :param value: The value to be inserted.
    """
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
    new_node.previous = current  # Point new_node's previous to the current node (we're inserting after it)

    # If current is not the last node, update the next node's previous to point to the new node
    if current.next:
        current.next.previous = new_node # Update next node's previous to new_node
    else:
        end = new_node  # If inserting at the end, update the global end pointer

    current.next = new_node  # Link the current node's next to the new node

# --------------------------- DELETION OPERATIONS ---------------------------

# Function to delete the first node
def del_first_node():
    """
    Delete the first node in the doubly linked list.
    """
    global start, end  # Declare that we are using the global start and end pointers of the doubly linked list

    if start is None:
        # If the start is None, the list is empty
        print("List is empty!")  # Inform the user that deletion isn't possible
    elif start.next is None:
        # If there is only one node in the list (start has no next node)
        start = end = None  # Remove the only node by setting both start and end to None
    else:
        # If there are multiple nodes in the list
        start = start.next      # Move the start pointer to the second node (next of current start)
        start.previous = None       # Remove the backward link from the new start node to completely detach the old first node
  # Remove backward link

# Function to delete the last node
def del_last_node():
    """
    Delete the last node in the doubly linked list.
    """
    global start, end  # Declare we are using global start and end pointers

    if start is None:
        # If the list is empty (no nodes), there is nothing to delete
        print("List is empty!")

    elif start.next is None:
        # If there is only one node in the list (start has no next node)
        # It means start and end both point to the same single node
        start = end = None  # Remove the only node by setting both to None

    else:
        # If there are two or more nodes in the list
        end = end.previous        # Move the end pointer to the previous node (second-last node becomes the new last)
        end.next = None       # Break the link to the old last node (new end's next should be None)

# Function to delete node at a given position
def del_at_pos(p):
    """
    Delete a node at a given position.
    
    :param p: Position of the node to be deleted.
    """
    global start, end  # Use the global start and end pointers
    if p > count_nodes() or p < 1:
        # If the given position is greater than total nodes or less than 1, it's invalid
        print("Invalid position!")
        return  # Exit the function
    if p == 1:
        # If position is 1, delete the first node
        del_first_node()
        return
    elif p == count_nodes():
        # If position is the last node, delete the last node
        del_last_node()
        return
    
    current = start  # Start traversing from the beginning of the list
    i = 1  # Position counter
    while i < p:
        current = current.next  # Move to the next node
        i += 1  # Increment position
    current.previous.next = current.next  # Update the link of the previous node to skip the current node
    current.next.previous = current.previous    # Update the link of the next node to skip the current node
    current.next = current.previous = None    # Clear the pointers of the current node (disconnect it fully)

# Function to delete a node by its value
def del_at_elem(elem):
    """
    Delete a node containing a specific value.
    
    :param elem: The value of the node to be deleted.
    """
    global start, end  # Use global pointers to access and update the doubly linked list
    current = start  # Start from the beginning of the list
    # Traverse the list to find the node with the matching data
    while current and current.data != elem:
        current = current.next  # Move to the next node
    # If the element is not found in the list
    if not current:
        print("Element not found!")
        return  # Exit the function
    # If the node to delete is the first node
    if current == start:
        del_first_node()  # Call the function to delete the first node

    # If the node to delete is the last node
    elif current == end:
        del_last_node()  # Call the function to delete the last node
    # If the node is somewhere in the middle of the list
    else:
        current.previous.next = current.next  # Link the previous node to the next node
        current.next.previous = current.previous  # Link the next node back to the previous node
        current.next = current.previous = None  # Disconnect the current node completely from the list

# --------------------------- UTILITY FUNCTIONS ---------------------------

# Function to count the total number of nodes in the list
def count_nodes():
    """
    Count the total number of nodes in the doubly linked list.
    
    :return: The total count of nodes.
    """
    current, count = start, 0
    while current:          # Traverse until end
        count += 1
        current = current.next
    return count

# Function to display all nodes in the list
def display():
    """
    Display all the elements of the doubly linked list.
    """
    # Start from the beginning of the list
    current = start
    # If the list is empty, notify the user and return
    if current is None:
        print("List is empty.")
        return
    # If the list has elements, print a heading
    print("Doubly Linked List:", end=" ")

    # Traverse the list from start to end
    while current:
        # Print the current node's data followed by a connector
        print(current.data, end=" <-> ")
        # Move to the next node
        current = current.next
    # After reaching the end of the list, print 'None' to indicate the end
    print("None")

# Function to search for an element and return its position
def found(elem):
    """
    Search for an element in the doubly linked list and return its position.
    
    :param elem: The element to search for.
    :return: The position of the element in the list, or -1 if not found.
    """
    current, pos = start, 1
    while current:
        if current.data == elem:
            return pos      # Element found
        current = current.next
        pos += 1
    return -1               # Element not found

# Menu-driven program for doubly linked list operations

while True:
    print("\n------ Doubly Linked List Menu ------")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Insert Before Element")
    print("5. Insert After Element")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Delete at Position")
    print("9. Delete by Element")
    print("10. Search for Element")
    print("11. Count Nodes")
    print("12. Display List")
    print("13. Exit")

    choice = input("Enter your choice (1-13): ")

    if choice == '1':
        val = int(input("Enter value to insert at beginning: "))
        insert_at_beginning(val)
        display()

    elif choice == '2':
        val = int(input("Enter value to insert at end: "))
        insert_at_end(val)
        display()

    elif choice == '3':
        pos = int(input("Enter position to insert: "))
        val = int(input("Enter value to insert: "))
        insert_at_position(pos, val)
        display()

    elif choice == '4':
        target = int(input("Enter target element to insert before: "))
        val = int(input("Enter value to insert: "))
        insert_before_element(target, val)
        display()

    elif choice == '5':
        target = int(input("Enter target element to insert after: "))
        val = int(input("Enter value to insert: "))
        insert_after_element(target, val)
        display()

    elif choice == '6':
        del_first_node()
        display()

    elif choice == '7':
        del_last_node()
        display()

    elif choice == '8':
        pos = int(input("Enter position to delete: "))
        del_at_pos(pos)
        display()

    elif choice == '9':
        elem = int(input("Enter element to delete: "))
        del_at_elem(elem)
        display()

    elif choice == '10':
        elem = int(input("Enter element to search: "))
        pos = found(elem)
        if pos == -1:
            print("Element not found!")
        else:
            print(f"Element found at position {pos}.")
            display()

    elif choice == '11':
        print(f"Total nodes in the list: {count_nodes()}")
        display()

    elif choice == '12':
        display()

    elif choice == '13':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 13.")
 