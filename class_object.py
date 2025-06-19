from dataclasses import dataclass, field

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

@dataclass
class ClassRelationships:
    inheritances: list[str] = field(default_factory=list)
    associations: list[str] = field(default_factory=list)     # get passed another object or refer to it
    compositions: list[str] = field(default_factory=list)     # one class created and manage the other
    aggregations: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)     # used an object just inside a method

@dataclass
class ClassObject:
    class_name: str
    class_variables: list[tuple[str, str]] = field(default_factory=list)     # [ ( variable name , data type ) ]
    class_functions: list[tuple[str, str, str]] = field(default_factory=list)     # [ ( modifier, function(param) , return_type ) ]
    class_relationships: ClassRelationships = field(default_factory=ClassRelationships)
