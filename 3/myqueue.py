#3.4
from stack import Stack

class MyQueue:
    def __init__(self,size):
        self.s_old = Stack(size=size)
        self.s_new = Stack(size=size)
    
    def add(self,data:int):
        self.s_new.push(data)
        return 
    
    def migrate_to_old(self):
        if self.s_old.is_null():
            while not self.s_new.is_null():
                self.s_old.push(self.s_new.pop())
    
    def remove(self):
        self.migrate_to_old()
        return self.s_old.pop()


if __name__ == "__main__":
    arr = [1,2,3,4,3,2,4,1,2,4,23]
    q = MyQueue(50)

    for item in arr:
        q.add(item)
    
    print(q.remove()) # 1
    print(q.remove()) # 2
