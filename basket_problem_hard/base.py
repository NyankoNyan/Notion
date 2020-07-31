

class Node:
    nodes = []
    search_index = {}
    
    def __init__(self, name=None, chapter=None):
        self.name = name
        self.chapter = chapter
        self.components = []
        self.__reg()
        
    def __reg(self):        
        Node.nodes.append(self)
        Node.search_index[self.get_key()] = self
        
    def get_key(self):
        return self.pack_key(self.name, self.chapter)
    
    def component(self, name):
        return [comp for comp in self.components if comp.node.name==name][0]
    
    @staticmethod
    def pack_key(name, chapter=None):
        return name + ( "" if chapter is None else ":" + chapter)
    
    @staticmethod
    def unpack_key(key:str):
        key_parts = key.split()
        return key_parts[0], None if len(key_parts) < 2 else key_parts[1]
    
    @staticmethod
    def find(name=None, chapter=None):
        return Node.search_index[Node.pack_key(name, chapter)]
        

class Component:
    def __init__(self, node):
        self.node = node
        
