#2-3
from binary_tree import BinaryTree,Node
import random

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
    print(tree.root.data)
    print(tree.root.right.data)
    print(tree.root.left.data)
    print(arr)