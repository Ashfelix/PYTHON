

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def in_order_dfs(node):
    if node == None:
        return 
    in_order_dfs(node.left)
    print(node.data,end= ' ')
    in_order_dfs(node.right)
def insert(root,key):
        

# Creating the tree
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
print("",end='')
in_order_dfs(root)

        