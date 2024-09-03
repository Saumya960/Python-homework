#Question1
import random
dice = int(input("How many dice to be rolled? "))
sum = 0
for i in range(dice):
     rolls = random.randint(1,6)
     sum += rolls
     print(rolls)
print(f"The sum of all dice roll is: {sum}")


#Question2
numbers =  []
while True:
     user_input = input("Enter a number: ")
     if user_input == "":
          break
     number = int(user_input)
     numbers.append(number)

numbers.sort(reverse = True)
greatest_numbers = numbers[:5]
print("The five greatest numbers are:")
for number in greatest_numbers:
     print(number)


#Question3
user_input = int(input("Enter an integer: "))
prime_num = True
if user_input <= 1:
     prime_num = False
else:
     for i in range (2, user_input):
          if user_input % i == 0:
               prime_num = False
               break

if prime_num:
     print(f"{user_input} is a prime number.")
else:
     print(f"{user_input} is not a prime number.")



