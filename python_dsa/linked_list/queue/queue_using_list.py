
# Initialize the queue with size
front, rear = -1, -1
size = int(input('Enter size of the queue: '))

# Function to insert an item into the queue
def insert(queue, item):
    """
    Insert an item into the queue.
    
    :param queue: The queue into which the item will be inserted.
    :param item: The item to be inserted into the queue.
    """
    global front, rear
    # Check if the queue is full (overflow)
    if rear >= size - 1:
        print("Overflow")  # Queue is full, cannot insert more items
    elif front == -1:  # If the queue is empty, initialize front and rear
        front = rear = 0
        queue[rear] = item  # Insert the item at the rear
    else:
        rear += 1  # Increment the rear to the next available position
        queue[rear] = item  # Insert the item at the rear

# Function to delete an item from the queue
def delete(queue):
    """
    Delete an item from the queue.
    
    :param queue: The queue from which an item will be deleted.
    """
    global front
    # Check if the queue is empty (underflow)
    if front == -1 or front > rear:
        print("Underflow")  # No items to delete, queue is empty
    else:
        print('Deleted item is:', queue[front])  # Display the deleted item
        front += 1  # Increment front to point to the next item

# Function to display the front element of the queue
def display_front(queue):
    """
    Display the front element of the queue.
    
    :param queue: The queue whose front element will be displayed.
    """
    global front
    # Check if the queue is empty
    if front == -1 or front > rear:
        print('Empty')  # No items in the queue
    else:
        print("Front is:", queue[front])  # Display the front item

# Function to display all elements in the queue
def display(queue):
    """
    Display all elements in the queue from front to rear.
    
    :param queue: The queue whose elements will be displayed.
    """
    global front
    # Check if the queue is empty
    if front == -1 or front > rear:
        print("Empty")  # No items to display
    else:
        print('Elements are:')
        # Display the elements from front to rear
        for i in range(front, rear + 1):
            print(queue[i], end=" ")  # Print each element
        print()  # Print newline after displaying elements

# Main menu for queue operations
queue = [0] * size
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Display the front element")
    print("4. Display all queue elements")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = int(input("Input the element to add to the queue: "))
        insert(queue, item)  # Call the insert function
    elif choice == 2:
        delete(queue)  # Call the delete function
    elif choice == 3:
        display_front(queue)  # Call the display_front function
    elif choice == 4:
        display(queue)  # Call the display function
    elif choice == 5:
        break  # Exit the loop and quit the program
    else:
        print("Invalid choice")  # Invalid input handling
