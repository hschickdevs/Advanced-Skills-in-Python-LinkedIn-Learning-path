# The following code example is for the "Factory" design pattern, which encapsulates object creation.

# Scenario: Pet shop used to sell only dogs, but now needs to be able to sell cats too:

class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):

    """The factory method"""
    
    pets = dict(dog=Dog(name="Hope"), cat=Cat("Peace"))

    return pets[pet]

d = get_pet(pet="dog")
print(d.speak())

c = get_pet(pet="cat")
print(c.speak())
