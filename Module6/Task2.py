import random
def dice_roll(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("Enter the number of sides: "))
    result = 0
    max_num = sides

    while result != max_num:
        result = dice_roll(sides)
        print(f"Rolled : {result}")

if __name__ == '__main__':
    main()