
class BinaryTree:
    def __init__(self,root=None):
        self.root:Node = root
    

class Node:
    def __init__(self,data):
        self.data = data
        self.right:Node = None
        self.left:Node = None