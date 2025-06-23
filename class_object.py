# Small table for relationships
'''
| Relationship | Symbol | Description                        | Lifespan      |
| ------------ | ------ | ---------------------------------- | ------------- |
| Association  | `→`    | General usage or reference         | Independent   |
| Inheritance  | `▷`    | One class extends another          | Hierarchical  |
| Composition  | `◆→`   | Strong ownership                   | Same lifespan |
| Aggregation  | `◇→`   | Weak ownership                     | Independent   |
| Dependency   | `--->` | Temporary use (method param, etc.) | Temporary     |
'''

# Small example of relationships
'''
class Engine:
    pass
    
shared_engine = Engine()

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition (Car owns Engine)

class Driver:
    def drive(self, car):       # Dependency (uses Car temporarily)
        print("Vroom")

class ElectricCar(Car):         # Inheritance
    pass

class Bus:
    def __init__(self, engine):
        self.engine = engine  # aggregation

class Boat:
    def __init__(self, engine):
        self.engine = engine  # aggregation
'''

from dataclasses import dataclass, field
from enum import Enum

class RelationType(Enum):
    INHERITANCE = ("onormal", "solid")
    ASSOCIATION = ("vee", "solid")
    COMPOSITION = ("diamond", "solid")
    AGGREGATION = ("odiamond", "solid")
    DEPENDENCY = ("vee", "dashed")

@dataclass
class Relation:
    source_class: str
    target_class: str
    relation_type: RelationType

    def get_arrow_style(self):
        return self.relation_type.value

class AccessModifier(Enum):
    PUBLIC = "+"
    PRIVATE = "-"
    PROTECTED = "#"

@dataclass
class ClassObject:
    class_name: str
    class_variables: list[tuple[str, str]] = field(default_factory=list)     # [ ( variable name , data type ) ]
    class_functions: list[tuple[AccessModifier, str, str]] = field(default_factory=list)     # [ ( modifier, function(param) , return_type ) ]
    class_relationships: list[Relation] = field(default_factory=list)
