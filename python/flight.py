class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():  # if self.open_seats == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        # print(self.capacity - len(self.passengers))
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Jan", "Strager", "Devon", "Elon"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seat for {person}")

# print(flight.passengers)
