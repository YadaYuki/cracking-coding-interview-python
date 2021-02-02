# 2.6
from linked_list import LinkedList,Node,initialize_linked_list_from_array

def is_palindrome(a:LinkedList,b:LinkedList) -> bool:
    if a.length != b.length:
        return False
    
    na,nb = a.head,b.tail

    while (na is not None) and (nb is not None):
        if na.data != nb.data:
            return False
        na,nb = na.next,nb.prev

    return True


if __name__ == "__main__":

    a,b = [7,1,6],[6,1,7]
    
    la,lb = initialize_linked_list_from_array(a),initialize_linked_list_from_array(b)
    
    print(is_palindrome(la,lb)) # True