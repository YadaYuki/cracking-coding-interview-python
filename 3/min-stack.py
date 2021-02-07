#3-2
import random
class StackNode:
    def __init__(self,data:int,min_data:int):
        self.data = data
        self.min_data = min_data


class Stack:
    def __init__(self,size:int):
        self.size = size
        self.data_arr:list(StackNode) = [None for _ in range(size)]
        self.idx = -1

    def pop(self):
        if self.idx == -1:
            return None
        pop_data = self.data_arr[self.idx]
        self.idx -= 1
        return pop_data
    
    def min(self):
        if self.idx == -1:
            return None
        return self.data_arr[self.idx].min_data
    
    def push(self,data:int):        
        stack_node:StackNode = None
        
        if self.min() == None:
            stack_node = StackNode(data,data)
        elif data < self.min():
            stack_node = StackNode(data,data)
        else:
            stack_node = StackNode(data,self.min())
        
        self.idx += 1
        self.data_arr[self.idx] = stack_node

        return 
    
    def __str__(self):
        if self.idx == -1:
            return "This Stack is null"
        s = ""
        for i in range(self.idx):
            s += "{}->".format(self.data_arr[i].data)
        return s



if __name__ == "__main__":
    stack_size = 50
    s = Stack(size = stack_size)
    for item in range(stack_size):
        
        s.push(random.randint(-100,100))
    print(s.min())
    print(s)
    