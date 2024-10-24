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

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def main():
    my_car = Car("ABC-123", 142)
    my_car.properties()

    my_car.accelerate(30)
    print(f"\nAfter accelerating 30km/h, Current speed: {my_car.current_speed} km/h")

    my_car.drive(1.5)
    print(f"\nAfter driving 1.5 hours, Travelled Distance: {my_car.travelled_distance} km")

    my_car.accelerate(70)
    print(f"\nAfter accelerating 70km/h,Current speed: {my_car.current_speed} km/h")

    my_car.drive(2)
    print(f"\nAfter driving 2 hours, Travelled Distance: {my_car.travelled_distance} km")

    my_car.accelerate(-200)
    print(f"\nFinal speed: {my_car.current_speed} km/h")

    my_car.properties()


main()



