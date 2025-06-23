from class_object import ClassObject, Relation, RelationType, AccessModifier
from uml_generator import UmlGenerator

# class A
name_a = "A"

variables_a = [
    ("A1", "string"),
    ("A2", "integer")
]

functions_a = [
    (AccessModifier.PUBLIC, "lol_a1(o: str, m: int, g: bool)", "int"),
    (AccessModifier.PROTECTED, "lol_a2(l: str, o: int, l: bool)", "bool")
]

# relationships
inheritance_a = [Relation(source_class=name_a, target_class=target, relation_type=RelationType.INHERITANCE)
                 for target in ["Father_A", "Mother_A"]]

associations_a = [Relation(source_class=name_a, target_class=target, relation_type=RelationType.ASSOCIATION)
                  for target in ["C", "D"]]

compositions_a = [Relation(source_class=name_a, target_class=target, relation_type=RelationType.COMPOSITION)
                  for target in ["E"]]

aggregations_a = [Relation(source_class=name_a, target_class=target, relation_type=RelationType.AGGREGATION)
                  for target in ["F", "G"]]

dependencies_a = [Relation(source_class=name_a, target_class=target, relation_type=RelationType.DEPENDENCY)
                  for target in ["H"]]

# all relations combined
all_relations = inheritance_a + associations_a + compositions_a + aggregations_a + dependencies_a

# create ClassObject
my_class_object = ClassObject(
    class_name=name_a,
    class_variables=variables_a,
    class_functions=functions_a,
    class_relationships=all_relations
)

uml = UmlGenerator(my_class_object)
uml.add_class_box()
uml.generate_inheritances()
uml.render_graph()