class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Sandro", "Felipe","Rafael", "Daniele"]

for person in people:
    
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaiable seats for {person}")