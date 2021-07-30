import copy

class Prototype:
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self) -> None:
        self.name = "Range Rover"
        self.color = "White w/ Black Rims"
        self.options = "Sport Package"

    def __str__(self) -> str:
        return f"{self.name} {self.color} {self.options}"

c = Car()
prototype = Prototype()
prototype.register_object(name='Range Rover', obj=c)

clone_1 = prototype.clone('Range Rover')

print(clone_1)