#4-3
from binary_tree import BinaryTree,Node
from generate_binary_tree import create_minimal_bst
import random

map = {}


# TODO: refactarize

def get_depth(root:Node):
    if root == None:
        return 0    
    val = 1 + max(get_depth(root.right),get_depth(root.left))
    if map.get(val) == None:
        map[val] = [root.data]
    else:
        map[val].append(root.data)
    return val

def depth_list():
    pass

def depth_list_recursion():
    pass


if __name__ == "__main__":
    arr = [random.randint(0,100) for _ in range(7)]
    arr.sort()
    n = create_minimal_bst(arr,0,len(arr)-1)
    print(get_depth(n))
    print(map)
    tree = BinaryTree(root=n)