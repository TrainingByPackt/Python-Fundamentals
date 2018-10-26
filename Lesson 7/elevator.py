class Elevator:
    occupancy_limit = 8

    def __init__(self, occupants):
        if occupants > self.occupancy_limit:
            print("The maximum occupancy limit has been exceeded."
                  f" {occupants - self.occupancy_limit} occupants must exit the elevator.")
        self.occupants = occupants


elevator1 = Elevator(6)
print("Elevator 1 occupants:", elevator1.occupants)
elevator2 = Elevator(10)
print("Elevator 2 occupants:", elevator2.occupants)
