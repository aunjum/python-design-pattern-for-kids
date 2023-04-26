class Memento:
    def __init__(self, state):
        self._state = state
    
    def get_state(self):
        return self._state
    
class Originator:
    def __init__(self):
        self._state = None
    
    def set_state(self, state):
        self._state = state
    
    def create_memento(self):
        return Memento(self._state)
    
    def restore_memento(self, memento):
        self._state = memento.get_state()
    
class Caretaker:
    def __init__(self):
        self._mementos = []
    
    def add_memento(self, memento):
        self._mementos.append(memento)
    
    def get_memento(self, index):
        return self._mementos[index]
    
originator = Originator()
caretaker = Caretaker()

# Set the state of the Originator
originator.set_state("State 1")

# Create a Memento and add it to the Caretaker
memento = originator.create_memento()
caretaker.add_memento(memento)

# Change the state of the Originator
originator.set_state("State 2")

# Create another Memento and add it to the Caretaker
memento = originator.create_memento()
caretaker.add_memento(memento)

# Restore the first Memento
memento = caretaker.get_memento(0)
originator.restore_memento(memento)

# Check the state of the Originator
print(originator._state) # Output: State 1
