class Node:
    def __init__(self,data:int):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList: 

    def __init__(self,head_data:int):
        self.head = Node(head_data)
        self.tail = self.head

    def append_node(self,data:int):
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def __str__(self):
        s = ""
        node = self.head
        while node != None:
            s += "{}->".format(node.data)
            node = node.next
            
        return s
