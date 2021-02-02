class Node:
    def __init__(self,data:int):
        self.data = data
        self.prev:Node = None
        self.next:Node = None


class LinkedList: 

    def __init__(self,head_data:int):
        self.head = Node(head_data)
        self.tail = self.head
        self.length = 1

    def append_node(self,data:int):
        self.tail.next = Node(data)
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
    
    def get_node(self,k:int) -> Node:
        n = self.head
        for i in range(k):
            n = n.next
        return n
