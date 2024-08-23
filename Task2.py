user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of thr circle {radius} is: {area: .2f}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The are of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")