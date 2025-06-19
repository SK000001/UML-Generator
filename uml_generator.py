from class_object import ClassObject
from graphviz import Digraph

def generate_uml(class_obj: ClassObject):    
    dot = Digraph()
    
    cls_name = class_obj.class_name
    label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD BGCOLOR="lightgray"><B>{cls_name}</B></TD></TR><TR><TD ALIGN="LEFT">"""

    for var_name, var_type in class_obj.class_variables:
        label += f'+ {var_name} : {var_type}<BR ALIGN="LEFT"/>\n'
    
    label += f"""</TD></TR><TR><TD ALIGN="LEFT">"""
    for mod, func_name, return_type in class_obj.class_functions:
        label += f'{mod} {func_name} : {return_type}<BR ALIGN="LEFT"/>\n'
    
    label += "</TD></TR></TABLE>>" 
    
    dot.node(cls_name, label=label, shape="plaintext")
    
    for inher in class_obj.class_relationships.inheritances:
        dot.node(inher, shape="box")
        dot.edge(inher, cls_name, arrowhead="onormal")
        
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