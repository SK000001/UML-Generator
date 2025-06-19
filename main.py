from class_object import ClassObject, ClassRelationships
from uml_generator import generate_uml

# class A
name_a = "A"
variables_a = [
    ("A1", "string"),
    ("A2", "integer")
]
functions_a = [
    ("lol_a1(o: str, m: int, g: bool)", "int"),
    ("lol_a2(l: str, o: int, l: bool)", "bool")
]

inheritance_a = ["Father_A", "Mother_A"]
associations_a = ["C", "D"]
compositions_a = ["E"]
aggregations_a = ["F", "G"]
dependencies_a = ["H"]


relationships = ClassRelationships(inheritances=inheritance_a, associations=associations_a, compositions=compositions_a, aggregations=aggregations_a, dependencies=dependencies_a)
class_a = ClassObject(name_a, variables_a, functions_a, relationships)

generate_uml(class_obj=class_a)