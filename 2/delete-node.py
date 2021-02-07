# 2.3
from linked_list import LinkedList,Node

def delete_node(linked_list:LinkedList,i:int):
    node = linked_list.get_node(i)
    if node == None:
        return 
    node.data = node.next.data
    node.next = node.next.next
    return 

if __name__ == "__main__":
    # Initialize LinkedList
    l = LinkedList(head_data=1)
    data = [1,2,3,4,2,1,3,5,2,2,4]
    for item in data:
        l.append_node(item)
    
    print("Before:{}".format(l)) 
    delete_node(l,2)
    print("After :{}".format(l))
