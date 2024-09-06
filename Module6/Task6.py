import math

def pizza_sqm(diameter,price):
    radius = diameter / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    pizza_sqm = price / area_m2
    return pizza_sqm

diameter1 = float(input("Enter the diameter of pizza1 (cm): "))
price1 = float(input("Enter the price of pizza1 (€): "))
diameter2 = float(input("Enter the diameter of pizza2 (cm): "))
price2 = float(input("Enter the price of pizza2 (€): "))

unit_price1 = pizza_sqm(diameter1, price1)
unit_price2 = pizza_sqm(diameter2, price2)

print(f"Unit price of pizza1 : {unit_price1:.2f} ")
print(f"Unit price of pizza2 : {unit_price2:.2f}")

if unit_price1 < unit_price2:
    print("Pizza1 offers better value.")
elif unit_price1 > unit_price2:
    print("Pizza2 offers better value.")