
class Node:
    def __init__(self,data):
        self.data = data
        self.right:Node = None
        self.left:Node = None

class BinaryTree:
    def __init__(self,root=None):
        self.root:Node = root
    
    # TODO:implement __str__

    def print_node(self,n:Node):
        if n != None:
            self.print_node(n.left)
            print(n.data)
            self.print_node(n.right)

    def print_tree(self):
        self.print_node(self.root)

