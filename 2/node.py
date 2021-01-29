class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None


class LinkedList: 

    def __init__(self,head_data:int):
        self.head = Node(head_data)
        self.tail = self.head

    def append_node(self,data:int):
        self.tail.next = Node(data)
        self.tail = self.tail.next



