
# Import packages
import random

# Read in lines from word.txt file and convert it into a list
with open("words.txt") as words_file:
    list_of_words = []
    for line in words_file:
        list_of_words.append(line)

# Get random item (word) from list and print greeting message
word = list_of_words[random.randint(0, len(list_of_words))]
print("Let's play Hangman!")

# Add dashes to an array that is the same length of the randomly generated word
# Uses the join function to turn the array into a string
dashes = ['_'] * (len(word) - 1)
print(''.join(dashes))

# Initialize variables
num_of_guesses = 0
wrong_guesses = 0
list_of_guesses = []

# Game loop
while True:
    # Prompts the user to enter a letter
    guess = input("Enter a letter to guess: ")

    # Makes sure the user only enters a letter as a guess
    if len(guess) == 1:

        # Checks to see if the letter has already been guessed
        # The guesses are added to a list and if the guess is in the
        # list a message that says so will be printed
        if guess in list_of_guesses:
            print("You have already guessed this letter!")

        # Code below only executes if the guess (letter) is in the word
        elif guess in word:
            print("Great guess!")

            # Increments the variable num_of_guesses by 1
            num_of_guesses += 1

            # Replaces the dashes with the correct guess
            # Example: _ _ _ -> _ a _
            for i, x in enumerate(word):
                if x is guess:
                    dashes[i] = guess
            guess_dashes = ''.join([str(x) + "" for x in dashes])
            print(guess_dashes)

            # Adds the user's guess to list_of_guesses
            list_of_guesses.append(guess)

            # Checks if the user won and got the right word
            if guess_dashes.isalpha():
                print("Congrats! You guessed the word " + str(word) + " in " + str(num_of_guesses) + " guesses!")
                break
        else:
            # Increments variables if the user's guess was incorrect
            num_of_guesses += 1
            wrong_guesses += 1

            # Prints wrong guess message and lets the user know how many guesses they have left
            # The guess is appended to the list list_of_guesses
            print("Sorry, wrong guess. You have " + str(6 - wrong_guesses) + " wrong guesses left")
            list_of_guesses.append(guess)

            # If the user gets to six wrong guesses the game finishes
            # The user is shown a message telling them they lost along with what the word was
            if wrong_guesses == 6:
                print("Sorry you lost :( The word was " + word)
                break

    # If the guess is not a single character, the user will be prompted
    # to guess a valid guess which is one letter
    else:
        print("Please enter a single character to guess")
