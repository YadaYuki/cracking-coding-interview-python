#7.11
import datetime

class Entry():
    def __init__(self,name:str):
        self.name = name
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def get_name(self):
        return self.name
    
    def get_created_at(self):
        return self.created_at
    
    def get_updated_at(self):
        return self.updated_at
    
    def set_name(self,name):
        self.name = name
    
    def set_updated_at(self):
        self.updated_at = datetime.datetime.now()
    


class File(Entry):
    def __init__(self,name,data,format):
        super().__init__(name)
        self.data = data
        self.format = format
        self.size = len(data) # TODO:change to sizeof
    
    def get_data(self):
        return self.data    

    def get_format(self):
        return self.format

    def get_size(self):
        return self.size
    
    def edit_file(self,data):
        self.set_data(data)
        self.set_updated_at()

        
    def set_data(self,data):
        self.data = data



class Folder(Entry):
    def __init__(self,name):
        super().__init__(name)
        self.children = []

    def add_entry(self,entry:Entry):
        self.children.append(entry)
        self.set_updated_at()

