import random

def roll_dice(number):
    i = 0
    while i < number:
        print(random.randint(1, 6))
        i += 1


print("Welcome to the Dice Rolling Simulator!")

while True:
    try:
        number = int(input("How many times would you like to roll the dice? "))
        if number < 0:
            print("please enter a positive number")
        else:
            roll_dice(number)
        


    except ValueError:
        print("please enter a positive number")


print("Thanks for playing the Dice Rolling Simulator!")