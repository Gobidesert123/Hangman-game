'''
This is how you import from another file, notice how you can import
two different things from the same file and import them in the same line
'''
from Hangman_art_Udemy import stages, logo
from Hangman_words import word_list
import random
print(logo)
print("Welcome to the hangman game")


# random word selected
random_word = random.choice(word_list)


display = []
# Making a list of the random_words to iterate over.
lst = list(random_word)

# Depending on the number of letters in the random_word, it would create those many "-".
for i in range(len(random_word)):
    display.append("-")

print(display)
# Starting off with 6 lives
lives = 6
already_guessed = []

# Used to keep the while loop going until condition is met
continuing = False


while not continuing:
    guess = input("What is your guess? ")
    if guess in already_guessed:
        print(f"You have already guessed the letter: {guess}")
        # This is here to counter the - that happens later on.
        lives += 1
    else:
        already_guessed.append(guess)
        # This prints the letters in the list of already_guessed and prints the characters of it.
        guesses = " , ".join(already_guessed)
        print(f"Your guesses are: {guesses}")
    # This guess is one of the elements in the list and if it is then it gives display at that index the same value
    for i in range(len(random_word)):
        if guess == lst[i]:
            display[i] = guess
            already_guessed.append(guess)

    # This checks if guess is in the list or not and if its not it would run this.
    if guess not in lst:
        lives -= 1
        print(f"You have guessed wrong, You have {lives} lives remaining")
        print(stages[lives])
        if lives == 0:
            print("You Lose")
            print(f"The word was {random_word}")
            continuing = True
    if "-" not in display:
        continuing = True
        print("You win")
    print(display)



# Note you could use if "-" not in display:
# This is used to check if something is in a variable/list ...



