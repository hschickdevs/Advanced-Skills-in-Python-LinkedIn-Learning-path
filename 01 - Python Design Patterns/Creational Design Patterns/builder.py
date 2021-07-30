# Create the classes for the various roles in the builder design pattern:
class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    """Abstract Builder"""
    def __init__(self) -> None:
        self.car = None
    
    def create_new_car(self):
        self.car = Car()

class RangeSportBuilder(Builder):
    """Concrete Builder -> provides parts, and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Range Rover"
    
    def add_tires(self):
        self.car.tires = "Offroad Tires"
    
    def add_engine(self):
        self.car.engine = "V8 Supercharged"

# Create the Product Class:
class Car():
    """The Product"""
    def __init__(self) -> None:
        self.model = None
        self.tires = None
        self.engine = None
    
    def __str__(self) -> str:
        return f"{self.model} {self.tires} {self.engine}"

builder = RangeSportBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)