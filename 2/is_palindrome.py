# 2.6
from linked_list import LinkedList,Node,initialize_linked_list_from_array

def is_palindrome(l:LinkedList) -> bool:
    return True


if __name__ == "__main__":
    l = initialize_linked_list_from_array([1,1,2,2,1,1])
    print(is_palindrome(l)) # True
    l = initialize_linked_list_from_array([1,1,2,1,1])
    print(is_palindrome(l)) # True