class Toy:
    def __init__(self, name):
        self.name = name
        
class ToyBox:
    def __init__(self):
        self.toys = []
        
    def add_toy(self, toy):
        self.toys.append(toy)
        
    def __iter__(self):
        return ToyBoxIterator(self.toys)

class ToyBoxIterator:
    def __init__(self, toys):
        self.toys = toys
        self.current_index = 0
        
    def __next__(self):
        if self.current_index >= len(self.toys):
            raise StopIteration
        toy = self.toys[self.current_index]
        self.current_index += 1
        return toy

#In this example, we have a Toy class that represents a toy, and a ToyBox class that represents 
# a box of toys. The ToyBox class has an add_toy() method that lets us add toys to the box.

#The interesting part is the __iter__() method. When we call this method on a ToyBox object, 
# it returns a ToyBoxIterator object, which is the iterator for the ToyBox. The ToyBoxIterator 
# class has a __next__() method, which returns the next toy in the ToyBox each time it's called.

#We can use this iterator to loop through the toys in the ToyBox:

toy_box = ToyBox()
toy_box.add_toy(Toy("Teddy Bear"))
toy_box.add_toy(Toy("Action Figure"))
toy_box.add_toy(Toy("Barbie Doll"))

for toy in toy_box:
    print("Playing with", toy.name)
