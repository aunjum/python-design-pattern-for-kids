class Car:
    def drive(self):
        pass

class RaceCar(Car):
    def drive(self):
        print("Zoom! I'm a race car!")

class PoliceCar(Car):
    def drive(self):
        print("Woo-woo! I'm a police car!")

class FireTruck(Car):
    def drive(self):
        print("Beep beep! I'm a fire truck!")

class CarFactory:
    def create_car(self, car_type):
        if car_type == "race":
            return RaceCar()
        elif car_type == "police":
            return PoliceCar()
        elif car_type == "fire":
            return FireTruck()
        else:
            raise ValueError("Invalid car type!")

# Create a car factory
factory = CarFactory()

# Create a race car using the factory
race_car = factory.create_car("race")
race_car.drive()  # Output: "Zoom! I'm a race car!"

# Create a police car using the factory
police_car = factory.create_car("police")
police_car.drive()  # Output: "Woo-woo! I'm a police car!"

# Create a fire truck using the factory
fire_truck = factory.create_car("fire")
fire_truck.drive()  # Output: "Beep beep! I'm a fire truck!"
class Car:
    def drive(self):
        pass

class RaceCar(Car):
    def drive(self):
        print("Zoom! I'm a race car!")

class PoliceCar(Car):
    def drive(self):
        print("Woo-woo! I'm a police car!")

class FireTruck(Car):
    def drive(self):
        print("Beep beep! I'm a fire truck!")

class CarFactory:
    def create_car(self, car_type):
        if car_type == "race":
            return RaceCar()
        elif car_type == "police":
            return PoliceCar()
        elif car_type == "fire":
            return FireTruck()
        else:
            raise ValueError("Invalid car type!")

# Create a car factory
factory = CarFactory()

# Create a race car using the factory
race_car = factory.create_car("race")
race_car.drive()  # Output: "Zoom! I'm a race car!"

# Create a police car using the factory
police_car = factory.create_car("police")
police_car.drive()  # Output: "Woo-woo! I'm a police car!"

# Create a fire truck using the factory
fire_truck = factory.create_car("fire")
fire_truck.drive()  # Output: "Beep beep! I'm a fire truck!"


# In this example, we have a base Car class and different subclasses representing specific types of cars (RaceCar, PoliceCar, and FireTruck). 
# Each subclass overrides the drive method with its own implementation.

# The CarFactory class is responsible for creating cars. It has a create_car method that takes a car type as input and returns 
# an instance of the corresponding car. The factory encapsulates the creation logic and hides it from the calling code.

# By using the factory, we can create cars without directly instantiating the specific car classes. We simply specify the 
# desired car type to the factory, and it creates the appropriate car object for us.

# This is the essence of the factory pattern, where the factory acts as a centralized entity responsible for creating objects 
# based on the requested type.