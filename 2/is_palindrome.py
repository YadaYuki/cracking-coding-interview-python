# 2.6
from linked_list import LinkedListUnidirectional,NodeUnidirectional
# ADD RECURSION

class Result:
    def __init__(self,is_palindrome:bool,node:NodeUnidirectional):
        self.node = node
        self.is_palindrome = is_palindrome


def is_palindrome_recurse(node:NodeUnidirectional,length:int) -> Result:
    
    if length == 1:
        return Result(True,node.next)
    
    elif length == 0 or node == None:
        return Result(True,node)
    
    res = is_palindrome_recurse(node.next,length - 2)

    if res.is_palindrome == False or res.node == None:
        return res
    
    list_is_palindrome = (res.node.data == node.data)
    
    res.node = res.node.next
    res.is_palindrome = list_is_palindrome

    return res

def is_palindrome(l:LinkedListUnidirectional) -> bool:
    r:Result = is_palindrome_recurse(l.head,l.length)
    return r.is_palindrome


if __name__ == "__main__":
    
    arr = [1,2,3,4,3,2,1]
    l = LinkedListUnidirectional(head_data=arr[0])
    for item in arr[1:]:
        l.append_node(item)
    print(is_palindrome(l))
        