from class_object import ClassObject, ClassRelationships
from uml_generator import generate_uml

# class A
name_a = "A"
variables_a = [
    ("A1", "string"),
    ("A2", "integer")
]
inheritance_a = ["B"]
associations_a = ["C", "D"]
aggregations_a = ["E"]

relationships = ClassRelationships(inheritances=inheritance_a, associations=associations_a, aggregations=aggregations_a)
class_a = ClassObject(name_a, variables_a, relationships)

generate_uml(class_obj=class_a)