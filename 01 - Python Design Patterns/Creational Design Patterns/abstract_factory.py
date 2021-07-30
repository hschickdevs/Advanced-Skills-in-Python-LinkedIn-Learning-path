class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""
    
    def get_pet(self):
        """returns a Dog object"""
        return Dog()

    def get_food(self):
        """returns a Dog food object"""
        return "Dog Food!"

class PetStore:
    """PetStore houses our abstract factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to dispaly the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}!")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")

# Create a concrete factory
factory = DogFactory()

# Create a pet store for housing our abstract factory.
shop = PetStore(factory)

# Invoke the utility method to show details of our pet
shop.show_pet()