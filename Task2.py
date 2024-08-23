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

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3
print(f"The sum of {num1}, {num2},{num3} is: {sum_of_numbers}")
print(f" The product of {num1}, {num2},{num3} is: {product_of_numbers}")
print(f" The average of {num1}, {num2},{num3} is: {average_of_numbers}")

