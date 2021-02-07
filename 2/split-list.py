# 2.4
from linked_list import LinkedList,Node
from random import randint

def split_linked_list(l:LinkedList,x:int):
    n = l.head
    tail:Node = l.tail
    while n.data >= X:
        l.head = n.next
        l.append_node(n.data)
        n = n.next

    previous:Node = None

    while n != None and tail != n:
        if n.data >= X:
            previous.next = n.next # delete n(Node) from l(LinkedList)
            l.append_node(n.data)
        else :
            previous = n
        n = n.next


if __name__ == "__main__":
    # Initialize LinkedList
    l = LinkedList(head_data=10)
    data = [randint(0,10) for i in range(40)]
    for item in data:
        l.append_node(item)
    X = 5
    print(l)
    split_linked_list(l,X)
    print(l)
