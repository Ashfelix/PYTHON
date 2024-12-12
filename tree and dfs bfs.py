class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def in_order_dfs(node):
        if node == None:
            return 
        in_order_dfs(node.left)
        print(node.data)
        in_order_dfs(node.right)
        
if __name__ == "__main__":
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    in_order_dfs(root)
