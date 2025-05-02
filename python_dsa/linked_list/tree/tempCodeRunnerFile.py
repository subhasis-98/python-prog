class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
n1=Node("root node")
n2=Node("right child node")
n3=Node("left child node")
n4=Node("left grandchild  node")

n1.left_child= n2
n1.right_child= n3
n2.left_child= n4

curr = n1
while curr :
    print(curr.data) 
    curr = curr.left_child
curr = n1
while curr:
    print(curr.data)
    curr= curr.right_child