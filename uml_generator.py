from class_object import ClassObject
from graphviz import Digraph

def generate_uml(class_obj: ClassObject):
    cls_name = class_obj.class_name
    
    dot = Digraph()
    dot.node(cls_name, shape="box")
    
    for inher in class_obj.class_relationships.inheritances:
        dot.node(inher, shape="box")
        dot.edge(inher, cls_name)
        
    for asso in class_obj.class_relationships.associations:
        dot.node(asso, shape="box")
        dot.edge(cls_name, asso, arrowhead="vee")
    
    for comp in class_obj.class_relationships.compositions:
        dot.node(comp, shape="box")
        dot.edge(cls_name, comp, arrowhead="diamond")
        
    for aggr in class_obj.class_relationships.aggregations:
        dot.node(aggr, shape="box")
        dot.edge(cls_name, aggr, arrowhead="odiamond")
        
    for dep in class_obj.class_relationships.dependencies:
        dot.node(dep, shape="box")
        dot.edge(cls_name, dep, style="dashed")
        
    dot.render("class_diagram", format="png")