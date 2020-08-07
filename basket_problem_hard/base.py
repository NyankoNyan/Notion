import sys

chapter = "common"

class EmptyNameError(Exception):
    pass


class NotionFabric:
    @staticmethod
    def get(name=None, chapter=None):
        if chapter == None:
            chapter = sys.modules[__name__].chapter
        try:
            return Notion.find(name, chapter)
        except EmptyNameError:
            pass
        except KeyError:
            pass
        return Notion(name, chapter)


class Notion:
    nodes = []
    search_index = {}
    
    def __init__(self, name=None, chapter=None):
        self.name = name
        if chapter == None:
            self.chapter = sys.modules[__name__].chapter
        else:
            self.chapter = chapter
        self.__reg()
        
    def _str(self):   
        text = ""
        if self.name == None:
            text = "Anonymous notion"
        else:
            text = f"Notion {self.name}:{self.chapter}"
        return text     
        
    def __str__(self):
        return self._str()
        
    def __reg(self):        
        Notion.nodes.append(self)
        try:
            Notion.search_index[self.get_key()] = self
        except EmptyNameError:
            pass            
        
    def get_key(self):
        return self.pack_key(self.name, self.chapter)
    
    @staticmethod
    def pack_key(name, chapter):
        if name == None or chapter == None:
            raise EmptyNameError()
        return name + ":" + chapter
    
    @staticmethod
    def unpack_key(key:str):
        key_parts = key.split()
        return key_parts[0], None if len(key_parts) < 2 else key_parts[1]
    
    @staticmethod
    def find(name=None, chapter=None):
        if chapter == None:
            chapter = sys.modules[__name__].chapter
        return Notion.search_index[Notion.pack_key(name, chapter)]
        

class Component:
    def __init__(self, node):
        self.node = node
    def __str__(self):
        return str(self.node)
        
        
class Derivative:
    def __init__(self):
        pass