from elevator import Elevator
class Building:
    def __init__(self, bottom, top, num):
        self.bottom_floor = bottom
        self.top_floor = top
        self.num_of_elevators = num
        self.elevators = []
        for i in range(self.num_of_elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, num, destination_floor):
        if num < 1 or num > self.num_of_elevators:
            print("Invalid elevator number")
            return
        print(f"Moving elevator {num}")
        self.elevators[num-1].go_to_floor(destination_floor)

