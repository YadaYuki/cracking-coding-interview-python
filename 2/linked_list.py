class NodeBidirectional:
    def __init__(self,data:int):
        self.data = data
        self.prev:NodeBidirectional = None
        self.next:NodeBidirectional = None

class LinkedListBidirectional: 

    def __init__(self,head_data:int):
        self.head = NodeBidirectional(head_data)
        self.tail = self.head
        self.length = 1

    def append_node(self,data:int):
        self.tail.next = NodeBidirectional(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.length += 1

    def __str__(self):
        s = ""
        node = self.head
        while node != None:
            s += "{}->".format(node.data)
            node = node.next
        return s
    
    def get_node(self,k:int) -> NodeBidirectional:
        n = self.head
        for _ in range(k):
            n = n.next
        return n

class NodeUnidirectional:
    def __init__(self,data:int):
        self.data = data
        self.next:NodeUnidirectional = None

class LinkedListUnidirectional: 

    def __init__(self,head_data:int):
        self.head = NodeUnidirectional(head_data)
        self.tail = self.head
        self.length = 1

    def append_node(self,data:int):
        self.tail.next = NodeUnidirectional(data)
        self.tail = self.tail.next
        self.length += 1

    def __str__(self):
        s = ""
        node = self.head
        while node != None:
            s += "{}->".format(node.data)
            node = node.next
        return s
    
    def get_node(self,k:int) -> NodeUnidirectional:
        n = self.head
        for _ in range(k):
            n = n.next
        return n

def initialize_linked_list_from_array(array)->LinkedListBidirectional:
    l = LinkedListBidirectional(head_data=array[0])
    for item in array[1:]:
        l.append_node(item)
    return l
