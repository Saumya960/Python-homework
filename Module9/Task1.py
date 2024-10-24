class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def properties(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")
j
def main():
    my_car = Car("ABC-123", 142)
    my_car.properties()

main()

ef accelerate(self, change_of_speed):
        # Adjust the current speed with the provided change, ensuring it's within the valid range
        self.current_speed += change_of_speed

        # Make sure speed does not exceed the maximum speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        # Ensure speed does not fall below 0
        elif self.current_speed < 0:
            self.current_speed = 0

