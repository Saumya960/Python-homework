#Question1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#Question2
while True:
    inches = int(input("Enter a value in inches: "))
    if inches < 0:
        print("Negative value entered")
        break

    centimeters = inches * 2.54
    print("inches is equal to ", centimeters)



