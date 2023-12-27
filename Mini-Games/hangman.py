# Hangman Game
import random

# List of possible words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "peach", "raspberry", "strawberry", "watermelon"]

#setup a random word
word = random.choice(words)

#display function
def display():
    display_string = ""
    for letter in word:
        if letter in gussed_list:
            display_string += letter
        else:
            display_string += "-"

    return (display_string)


num_guesses = int(input("How many guesses would you like? "))
gussed_list = []

while True:
    guess = str(input("Guess a letter: "))
    if len(guess) != 1:
        print("Please enter only a single letter.")
        continue
    gussed_list.append(guess)

    if guess in word:
        print ("Correct!")
        print(display())
    if guess not in word:
        print ("Incorrect!")
        print(display())
        num_guesses -= 1
        print(str(num_guesses) + " left")
    

    if num_guesses == 0 :
        print("good luck next game the word was" + word) 
        break
    if "-" not in display():
        print("You win!")
        break