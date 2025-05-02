# Node class represents an element in the linked list-based queue
class Node:
    def __init__(self, data):  # Constructor to initialize a new node
        self.data = data       # Store the data passed during node creation
        self.next = None        # Initially, the next pointer is None (indicating no next node)

# Initialize front and rear pointers to None, representing an empty queue
front = rear = None

# Function to insert a new element into the queue
def insert(data):
    global front, rear  # Access global front and rear pointers
    new_node = Node(data)  # Create a new node with the given data
    if front is None:  # If the queue is empty
        front = rear = new_node  # Both front and rear point to the new node
    else:
        rear.next = new_node  # Link the current last node to the new node
        rear = new_node       # Move the rear pointer to the new node

# Function to delete an element from the queue (remove the front element)
def delete():
    global front, rear  # Access global front and rear pointers
    if front is None:  # If the queue is empty (front is None)
        print("Queue Underflow")  # Indicate an underflow (queue is empty)
        return
    deleted = front.data  # Store the data of the element to be deleted (front element)
    front = front.next    # Move the front pointer to the next node
    if front is None:     # If the queue is now empty (front is None)
        rear = None       # Set rear to None as well (no elements left in the queue)
    return deleted        # Return the data of the deleted element

# Function to peek at the front element of the queue without deleting it
def peek():
    if front is None:  # If the queue is empty
        print("Queue is empty")  # Indicate that the queue is empty
        return
    return front.data  # Return the data of the front element

# Function to display all the elements in the queue
def display():
    if front is None:  # If the queue is empty
        print("Queue is empty")  # Indicate that the queue is empty
        return
    current = front  # Start from the front of the queue
    print("Queue is :")  # Print a label indicating that queue elements will follow
    while current:  # Traverse the entire queue (while there are nodes left)
        print(current.data, end="  ")  # Print the data of the current node
        current = current.next  # Move to the next node in the queue
    print()  # Print a newline after displaying all the elements

# Main loop to interact with the user and perform queue operations
while True:
    # Menu options for the user
    print("\n1.Insert")
    print("2.Delete")
    print("3.Display element at the front")
    print("4.Display all elements of the queue")
    print("5.Quit")
    
    choice = int(input("Enter your choice: "))  # Get the user's menu choice

    if choice == 1:  # If the user selects "Insert"
        data = int(input("Input the element for adding in queue : "))  # Get the data to insert
        insert(data)  # Call the insert function to add the data to the queue
    elif choice == 2:  # If the user selects "Delete"
        deleted = delete()  # Call the delete function and store the deleted element's data
        if deleted is not None:  # If an element was deleted (queue was not empty)
            print("Deleted element is ", deleted)  # Print the deleted element
    elif choice == 3:  # If the user selects "Display front element"
        front_element = peek()  # Call the peek function to view the front element
        if front_element is not None:  # If the queue was not empty
            print("Element at the front is", front_element)  # Print the front element
    elif choice == 4:  # If the user selects "Display all elements"
        display()  # Call the display function to print all queue elements
    elif choice == 5:  # If the user selects "Quit"
        print("Exiting...")  # Print a message to indicate exiting the program
        break  # Exit the while loop and terminate the program
    else:  # If the user enters an invalid choice
        print("Invalid choice. Please try again.")  # Indicate invalid input
