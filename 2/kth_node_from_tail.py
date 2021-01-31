from linked_list import LinkedList,Node

def get_kth_node_from_tail(linked_list:LinkedList,k:int) -> Node: 
    node = l.tail
    i = 1
    while i != k:
        if node == None:
            return
        node = node.prev
        i += 1
    return node

if __name__ == "__main__":
    # Initialize LinkedList
    l = LinkedList(head_data=1)
    data = [1,2,3,4,2,1,3,5,2,2,4]
    for item in data:
        l.append_node(item)
    
    print(get_kth_node_from_tail(l,3).data) # 2
    
    print(get_kth_node_from_tail(l,19)) # None

    print(get_kth_node_from_tail(l,11).data) # 1

