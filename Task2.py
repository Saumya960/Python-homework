#Question1
user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")

#Question2
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of thr circle {radius} is: {area: .2f}")

#Question3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The are of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")

#Question4
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3
print(f"The sum of {num1}, {num2},{num3} is: {sum_of_numbers}")
print(f" The product of {num1}, {num2},{num3} is: {product_of_numbers}")
print(f" The average of {num1}, {num2},{num3} is: {average_of_numbers}")

#Question5
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
#convert talents to grams
grams_from_talents = talents * pounds_per_talent * lots_per_pound * grams_per_lot
#convert pounds to grams
grams_from_pounds = pounds * lots_per_pound * grams_per_lot
#convert lots to gram
grams_from_lots = lots * grams_per_lot
total_grams = grams_from_talents + grams_from_pounds +  grams_from_lots
#convert grams to kilogram
kilograms = int(total_grams / 1000)
remaining_grams = total_grams % 1000
print(f"\nThe weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")


