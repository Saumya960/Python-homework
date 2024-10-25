from car import Car

car1 = Car("ABC-123", 142)

print(f'''
Registration number : {car1.registration_number} 
Maximum_Speed : {car1.maximum_speed} 
Current_Speed : {car1.current_speed}
Travelled_Distance : {car1.travelled_distance}
'''
      )

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f'Current Speed after acceleration: {car1.current_speed}')

car1.drive(1.5)
print(f"Travelled distance after driving 1.5 hours: {car1.travelled_distance}")

car1.accelerate(-200)

print(f'Final speed after emergency break : {car1.current_speed}')
print(f'Final travelled distance : {car1.travelled_distance}')
