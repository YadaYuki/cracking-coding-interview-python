
class Stack:
    def __init__(self,size:int):
        self.size = size
        self.data_arr:list(int) = [None for _ in range(size)]
        self.idx = -1
    
    def pop(self):
        if self.is_null():
            return None
        pop_data = self.data_arr[self.idx]
        self.idx -= 1
        return pop_data
    
    def push(self,data:int):    
        self.idx += 1
        self.data_arr[self.idx] = data
        return 

    def is_null(self):
        return self.idx == -1
    
    def __str__(self):
        if self.is_null():
            return "This Stack is null"
        s = ""
        for i in range(self.idx):
            s += "{}->".format(self.data_arr[i].data)
        return s


