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


#Question3
smallest = 0
largest = 0

while True:
    user_input = input("Enter a number : ")

    if user_input == "":
        break
    number = float(user_input)
    if smallest == 0 or number < smallest:
        smallest = number
    if largest == 0 or number > largest:
        largest = number
if smallest != 0 and largest != 0:
    print("Smallest number is:", smallest)
    print("Largest number is:", largest)
else:
    print("No numbers were entered.")


#Question4
import random

number_guess = random.randint(1, 10)
while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < number_guess:
            print("Your guess is too low.")
    elif user_guess > number_guess:
            print("Your guess is too high!")
    else:
            print("Won! You guessed the number!")
            break




#Question6
import random
N = 1000000
n = 0
iterator = 0

while iterator < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
    iterator += 1
print(4 * n / N)

