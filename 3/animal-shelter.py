#3.6
from linked_list import LinkedListUnidirectional,NodeUnidirectional
import random

CAT = 0
DOG = 1

class AnimalShelter:
    def __init__(self):
        self.data = LinkedListUnidirectional(CAT)

    def enqueue(self,animal:int):
        self.data.append_node(animal)
        return

    def dequeue_any(self):
        if self.is_null():
            return None
        dequeue_data = self.data.head
        self.data.head = dequeue_data.next # overwrite head data
        return dequeue_data.data

    def dequeue_cat(self):
        if self.is_null():
            return None
        n = self.data.head
        prev:NodeUnidirectional = None
        if n.data == CAT:
            self.dequeue_any()
            return 
        while n != None:
            if n.data == CAT:
                prev.next = n.next
                return 
            else:
                prev = n
            n = n.next
        return 
    
    def dequeue_dog(self):
        if self.is_null():
            return None
        n = self.data.head
        prev:NodeUnidirectional = None
        if n.data == DOG:
            self.dequeue_any()
            return 
        while n != None:
            if n.data == DOG:
                prev.next = n.next
                return 
            else:
                prev = n
            n = n.next
        return 

    def is_null(self):
        return self.data.head == None
    
    def __str__(self):
        return str(self.data)


if __name__ == "__main__":

    a = AnimalShelter()
    data = [random.randint(CAT,DOG) for i in range(50)]

    for item in data:
        a.enqueue(item)
    
    print(a)

    a.dequeue_cat()
    a.dequeue_cat()
    a.dequeue_dog()
    a.dequeue_any()

    print(a)