
import random
from car import Car

# Initialize 10 cars with random maximum speeds
cars = []
for i in range(10):
    registration_number = f"ABC-{ i +1}"
    max_speed = random.randint(100, 200)  # Random maximum speed between 100 and 200 km/h
    cars.append(Car(registration_number, max_speed))

# Race simulation
race_ongoing = True
while race_ongoing:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_ongoing = False
            break

# Display the final race results
print \
    (f"{'Registration': <12} | {'Max Speed (km/h)': <15} | {'Current Speed (km/h)': <20} | {'Travelled Distance (km)'}")
print("-" * 65)
for car in cars:
    print \
        (f"{car.registration_number: <12} | {car.maximum_speed: <15} | {car.current_speed: <20} | {car.travelled_distance}")
