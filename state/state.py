class State:
    def handle(self):
        pass

class MovingState(State):
    def handle(self):
        print("Car is moving")
        
class StoppedState(State):
    def handle(self):
        print("Car is stopped")
        
class TurningLeftState(State):
    def handle(self):
        print("Car is turning left")

class TurningRightState(State):
    def handle(self):
        print("Car is turning right")
        
class ToyCar:
    def __init__(self):
        self.state = StoppedState()
        
    def set_state(self, state):
        self.state = state
        
    def move(self):
        self.set_state(MovingState())
        self.state.handle()
        
    def stop(self):
        self.set_state(StoppedState())
        self.state.handle()
        
    def turn_left(self):
        self.set_state(TurningLeftState())
        self.state.handle()
        
    def turn_right(self):
        self.set_state(TurningRightState())
        self.state.handle()

#In this example, we define four different states 
# (MovingState, StoppedState, TurningLeftState, TurningRightState) 
# and a base State class that defines a handle() method that is implemented by each state.

#We also define a ToyCar class that has four methods (move(), stop(), turn_left(), turn_right()) 
# that change the state of the toy car and call the handle() method of the current state.

#We can then create a ToyCar object and call its methods to see how the state changes:

toy_car = ToyCar()
toy_car.stop()
toy_car.turn_left()
toy_car.move()
toy_car.turn_right()
