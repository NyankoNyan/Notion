from .base import Notion
from basket_problem_hard import proto
from basket_problem_hard.base import NotionFabric
from basket_problem_hard.proto import ComponentFabric, Names


def define_notion_full(notion:Notion):
    """Определить сущность - означает определить все её связи"""
    for linked_notion in proto.find_common_index(notion):
        define_link(notion, linked_notion)


def define_link(original:Notion, linked:Notion):
    if hasattr(linked, "type"):
        if linked.type == Names.INSTANCE:
            if linked.instance == original:
                instantiate_children(linked.prototype, linked.instance)
            elif linked.prototype == original:
                pass
            else:
                raise Exception()
        elif linked.type == Names.COMPONENT:
            if linked.parent == original:
                pass
            elif linked.child == original:
                pass
            else:
                raise Exception()
        else:
            raise Exception()
    else:
        raise Exception()
    
    
def instantiate_children(prototype, instance):
    for component in proto.find_index(Names.COMPONENT, 
                                      ComponentFabric.PARENT, prototype):
        inst_comp = get_component(instance, component.name)
        if not inst_comp:
            inst_comp = NotionFabric.get(name=component.name, 
                                         chapter=instance.chapter)
            comp_link = ComponentFabric.get(inst_comp, instance)            
    

def get_component(notion, comp_name):
    for component in proto.find_index(Names.COMPONENT, 
                                      ComponentFabric.PARENT, notion):
        if component.name == comp_name:
            return component
    return