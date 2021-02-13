#4-4
from binary_tree import BinaryTree,Node
import random

def get_depth(root:Node):
    if root == None:
        return 0
    return 1 + max(get_depth(root.right),get_depth(root.left))

def is_equilibrium(root:Node):
    if root == None:
        return True
    
    if abs(get_depth(root.left) - get_depth(root.right)) > 1:
        return False
    else:
        return is_equilibrium(root.right) and is_equilibrium(root.left)
    
def create_minimal_bst(arr,start,end):
    if start > end:
        return None
    mid = int((start+end)/2)
    n = Node(data=arr[mid])
    n.left = create_minimal_bst(arr,start,mid-1)
    n.right = create_minimal_bst(arr,mid+1,end)
    return n

if __name__ == "__main__":
    arr = [random.randint(0,100) for _ in range(11)]
    arr.sort()
    n = create_minimal_bst(arr,0,len(arr)-1)
    tree = BinaryTree(root=n)
    print(is_equilibrium(n)) # True
