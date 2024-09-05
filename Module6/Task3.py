def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    gallons = float(input("Enter a volume in gallons: "))
    if gallons < 0:
        print("Negative value entered")
        break

    liters = gallons_to_liters(gallons)
    print(f"{gallons:.2f} gallons is equal to {liters:.2f} liters." )

