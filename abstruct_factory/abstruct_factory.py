# Abstract Factory
class ToyFactory:
    def create_toy(self):
        pass

# Concrete Factory 1
class CarFactory(ToyFactory):
    def create_toy(self):
        return CarToy()

# Concrete Factory 2
class DollFactory(ToyFactory):
    def create_toy(self):
        return DollToy()

# Abstract Product
class Toy:
    def play(self):
        pass

# Concrete Product 1
class CarToy(Toy):
    def play(self):
        print("Playing with a car toy!")

# Concrete Product 2
class DollToy(Toy):
    def play(self):
        print("Playing with a doll toy!")

# Client code
car_factory = CarFactory()
doll_factory = DollFactory()

car_toy = car_factory.create_toy()
car_toy.play()  # Output: Playing with a car toy!

doll_toy = doll_factory.create_toy()
doll_toy.play()  # Output: Playing with a doll toy!



# In this example, we have an abstract factory ToyFactory and two concrete factories CarFactory and DollFactory. 
# Each factory implements the create_toy method to create a specific type of toy. The Toy class is the abstract product, 
# and CarToy and DollToy are the concrete products. Each product has its own play method.

# The client code demonstrates how to use the factories to create toys. It creates a CarFactory and a DollFactory, 
# and then uses each factory to create a specific toy. Finally, it calls the play method on each toy to simulate playing with them.

# Note that this example is simplified for clarity. In real-world scenarios, abstract factories and products can have more 
# complex structures and interactions.



