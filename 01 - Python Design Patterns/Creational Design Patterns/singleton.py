class Borg:
    """Borg class making class attributes global"""

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):

    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

# Create Singleton object:
x = Singleton(HTTP="Hyper Text Transfer Protocol")

print(x)

# Create another singleton object:
y = Singleton(SNMP="Single Network Management Protocol")
print(y)