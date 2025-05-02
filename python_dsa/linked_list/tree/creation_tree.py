# Define the Node class to represent each node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data       # Store the value or label of the node
        self.left = None       # Pointer to the left child node
        self.right = None      # Pointer to the right child node

# Create nodes with short but meaningful names
root_Node = Node("root node")               # Root of the binary tree
left_Child = Node("left child node")        # Left child of the root
right_Child = Node("right child node")      # Right child of the root
left_Grandchild = Node("left grandchild node")  # Grandchild (left of left_Child)

# Link the nodes to form the binary tree structure
root_Node.left = left_Child                  # Set left_Child as left of root
root_Node.right = right_Child                # Set right_Child as right of root
left_Child.left = left_Grandchild            # Set left_Grandchild as left of left_Child

# Traverse the left side of the tree starting from the root
current = root_Node                         # Start with the root node
while current:                             # Loop until there are no more left nodes
    print(current.data)                    # Print the data of the current node
    current = current.left                 # Move to the left child

# Traverse the right side of the tree starting again from the root
current = root_Node                         # Reset current to root
while current:                             # Loop until there are no more right nodes
    print(current.data)                    # Print the data of the current node
    current = current.right                # Move to the right child
