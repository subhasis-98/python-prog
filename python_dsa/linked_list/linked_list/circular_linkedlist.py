# Node class to represent each element in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data       # Store the data in the node
        self.next = None       # Pointer to the next node, initially None

# Initialize the start pointer to None (empty list)
start = None
end = None  # Declare the end pointer, needed to maintain last node reference

# Function to insert a node at the beginning of the circular linked list
def insertbeg(data):
    global start, end  # Declare start and end as global so we can modify them

    # Step 1: Create a new node with the provided data
    new_node = Node(data)

    # Step 2: Check if the list is currently empty
    if start is None:
        # Since the list is empty, the new node will be the only node in the list
        start = new_node             # Point start to the new node
        start.next = start           # Make the new node point to itself to form a circular link
        end = new_node               # Set the end pointer to the new node, as it's the only one
    else:
        # Step 3: List is not empty, so we need to:
        # - Traverse to the last node (whose next points to start)
        # - Insert the new node at the beginning
        # - Update links accordingly to maintain circular structure

        end = start                  # Start from the first node
        # Traverse the list to find the last node (node whose next is pointing to start)
        while end.next != start:
            end = end.next
        # Step 4: Insert the new node at the beginning
        end.next = new_node          # Last node now points to the new node
        new_node.next = start        # New node points to the current start node
        start = new_node             # Update start to point to the new beginning node

# Function to insert a node at the end of the circular linked list
def insertend(data):
    global start, end  # Use the global start and end pointers for list manipulation

    # Step 1: Create a new node with the given data
    new_node = Node(data)
    new_node = Node(data)
    


    # Step 2: Check if the circular linked list is empty
    if start is None:
        # If the list is empty, initialize it with the new node
        start = new_node             # The new node becomes the first node
        start.next = start           # The node points to itself, maintaining circular structure
        end = new_node               # Set end pointer to the new node as it's the only one
    else:
        # Step 3: If the list is not empty, we need to:
        # - Traverse the list to find the last node
        # - Insert the new node at the end
        # - Update the links to preserve the circular nature

        end = start                  # Begin from the start of the list

        # Traverse until we reach the last node (whose next points to start)
        while end.next != start:
            end = end.next

        # Step 4: Insert the new node at the end
        end.next = new_node          # Last node now points to the new node
        new_node.next = start        # New node points back to start to maintain the circle
        end = new_node               # Update end to point to the new last node

# Function to delete the first node in the circular linked list
def deletebeg():
    global start, end  # Use global variables for start and end of the circular list

    if start is None:
        # Case 1: If the list is empty, print message and return
        print('Empty')
        return
    
    elif start.next == start:
        # Case 2: Only one node exists (it points to itself)
        # After deletion, the list becomes empty
        start = end = None
    else:
        # Case 3: List contains more than one node

        end = start  # Start by assigning end to the first node temporarily

        # Traverse to the last node (the one whose next points to start)
        while end.next != start:
            end = end.next

        start = start.next     # Move start to the second node (which becomes the new start)
        end.next = start       # Update the last node's next pointer to point to new start

# Function to delete the last node in the circular linked list
def deleteend():
    global start , end # Use the global start pointer

    if start is None:
        # Case 1: If the list is empty, nothing to delete
        print('Empty')
        return

    current = previous = start  # Initialize both current and previous to the start node

    if start.next == start:
        # Case 2: Only one node exists (points to itself)
        # After deletion, the list becomes empty
        start = end = None
        return

    # Case 3: Traverse the list to find the last node
    # The last node is the one whose next pointer points to start
    while current.next != start:
        previous = current       # Move previous one step behind current
        current = current.next   # Move current to the next node
       

    # After the loop, current is at the last node and previous is at second last
    previous.next = start        # Make second last node point to start (new last node)

# Function to display the elements in the circular linked list
def display():
    if start is None:             # If the list is empty
        print("List is empty")
        return
    current = start
    while True:
        print(current.data, end="-->")  # Print current node data
        current = current.next          # Move to the next node
        if current == start:            # Stop when back at the start
            break
    print("(back to start)")

# Function to count the total number of nodes in the circular linked list
def countnode():
    if start is None:
        return 0
    curr, count = start, 1  # Initialize count to 1 as start node exists
    while curr.next != start:
        count += 1
        curr = curr.next
    return count

# Menu-driven loop to interact with the circular linked list
while True:
    print("\n====== Circular Linked List Menu ======")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display List")
    print("6. Count Nodes")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert at beginning: "))
        insertbeg(value)
    elif choice == 2:
        value = int(input("Enter value to insert at end: "))
        insertend(value)
    elif choice == 3:
        deletebeg()
    elif choice == 4:
        deleteend()
    elif choice == 5:
        print("List elements are:")
        display()
    elif choice == 6:
        print("Total number of nodes:", countnode())
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
