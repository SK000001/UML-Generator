from class_object import ClassObject, Relation, RelationType
from graphviz import Digraph

class UmlGenerator:
    # Generates uml for a single class currently
    def __init__(self, class_obj: ClassObject) -> None:
        self.class_obj = class_obj
        self.cls_name = class_obj.class_name
        
        self.dot = Digraph()
        
        self.label = f"""<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD BGCOLOR="lightgray"><B>{self.cls_name}</B></TD></TR><TR><TD ALIGN="LEFT">"""
        
    def add_class_box(self):
        for var_name, var_type in self.class_obj.class_variables:
            self.label += f'+ {var_name} : {var_type}<BR ALIGN="LEFT"/>\n'
        
        self.label += f"""</TD></TR><TR><TD ALIGN="LEFT">"""
        for access, signature, ret_type in self.class_obj.class_functions:
            self.label += f'{access.value} {signature} : {ret_type}<BR ALIGN="LEFT"/>\n'
            
        self.label += "</TD></TR></TABLE>>"
        self.dot.node(self.cls_name, label=self.label, shape="plaintext")
        
    def __generate_relation_node__(self, relation: Relation):
        self.dot.node(relation.target_class, shape="box")
        
        arrowhead, style = relation.get_arrow_style()
            
        self.dot.edge(relation.source_class, relation.target_class, arrowhead=arrowhead, style=style)
        
    def __generate_relationship__(self, relation_type: RelationType | None = None):
        """
        Generate relationships of a specific type or all relationships if None is passed.
        
        Args:
            relation_type: The type of relationship to generate, or None for all types.
        """
        
        for relation in self.class_obj.class_relationships:
            if relation_type is None or relation.relation_type == relation_type:
                self.__generate_relation_node__(relation)
                
    def generate_all_relationships(self):
        self.__generate_relationship__()
    
    def generate_inheritances(self):
        self.__generate_relationship__(RelationType.INHERITANCE)
        
    def generate_associations(self):
        self.__generate_relationship__(RelationType.ASSOCIATION)
        
    def generate_compositions(self):
        self.__generate_relationship__(RelationType.COMPOSITION)
        
    def generate_aggregations(self):
        self.__generate_relationship__(RelationType.AGGREGATION)
    
    def generate_dependencies(self):
        self.__generate_relationship__(RelationType.DEPENDENCY)
        
    def render_graph(self):
        self.dot.render("uml_diagram", format="png", view=True)
        
