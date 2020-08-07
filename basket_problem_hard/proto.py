import types
from . import base


class Names:
    COMPONENT = "component"
    COLLECTION = "collection"
    STAGE = "stage"
    INSTANCE = "instance"
    COMMON = "common"


class ComponentFabric:
    CHILD = "child"
    PARENT = "parent"
    @staticmethod
    def get(child, parent):
        notion = base.NotionFabric.get()
        notion.child = child
        notion.parent = parent
        notion.type = Names.COMPONENT
        notion._str = types.MethodType(component_str, notion)
        ComponentFabric.__add_to_index(notion)
        return notion
    
    @staticmethod
    def index():
        return {ComponentFabric.CHILD: {}, ComponentFabric.PARENT: {}}
    
    @staticmethod
    def __add_to_index(component):
        add_index(Names.COMPONENT, ComponentFabric.PARENT, component.parent, component)
        add_index(Names.COMPONENT, ComponentFabric.CHILD, component.child, component)
        

def component_str(self):
    return f"Link ({self.parent}->{self.child})"
        
        
class CollectionFabric:
    @staticmethod
    def get(content):
        notion = base.NotionFabric.get()
        notion.content = content
        notion.type = Names.COLLECTION
        return notion


class StageFabric:
    @staticmethod
    def get(parent, root=None):
        notion = base.NotionFabric.get()
        notion.parent = parent
        notion.root = root
        notion.type = Names.STAGE
        return notion
    
    
class InstanceFabric:
    INSTANCE = "instance"
    PROTOTYPE = "prototype"
    @staticmethod
    def get(instance, prototype):
        notion = base.NotionFabric.get()
        notion.instance = instance
        notion.prototype = prototype
        notion.type = Names.INSTANCE
        return notion
    
    @staticmethod
    def index():
        return {InstanceFabric.INSTANCE: {}, InstanceFabric.PROTOTYPE: {}}
    
    @staticmethod
    def __add_to_index(notion):
        add_index(Names.INSTANCE, InstanceFabric.PROTOTYPE, notion.prototype, notion)
        add_index(Names.INSTANCE, InstanceFabric.INSTANCE, notion.instance, notion)


link_indexes = {
    Names.COMMON: {Names.COMMON: {}},
    Names.COMPONENT: ComponentFabric.index(),
    Names.INSTANCE: InstanceFabric.index()
    }


def add_index(notion_type, key_field, key_value, link_value):
    type_indexes = link_indexes[notion_type]
    key_index = type_indexes[key_field]
    try:
        link_array = key_index[key_value]
    except KeyError:
        link_array = []
        key_index[key_value] = link_array
    if link_value not in link_array:
        link_array.append(link_value)    


def add_common_index(notion, other_notions):
    for other_notion in other_notions:
        add_index(Names.COMMON, Names.COMMON, notion, other_notion)
        
        
def find_index(notion_type, key_field, key_value):
    type_indexes = link_indexes[notion_type]
    key_index = type_indexes[key_field]
    try:
        return key_index[key_value]
    except KeyError:
        return []


def find_common_index(notion):
    return find_index(Names.COMMON, Names.COMMON, notion)