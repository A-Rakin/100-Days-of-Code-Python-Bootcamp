import random
import hangman_words
import hangman_art 

#Import the logo from hangman_art.py and print it at the start of the game.

from hangman_art import logo
print(logo)

#Randomley choose a word form the word_list and assign it to a variable
choosen_word = random.choice(hangman_words.word_list)

lives = 6

#print(choosen_word)

#Create blanks
display = []

for letter in range(len(choosen_word)):
    display += "_"

end_of_game = False

#Ask the user to guess a letter and assign their answer to a variable called user_choice. Make sure the guess is in lowercase
while not end_of_game:
    user_choice = input("Guess a Word:\n").lower()

    if user_choice in display:
        print(f"You've already guessed {user_choice}")

#Check if the letter the user guessed (guess) is one of the letters in the chosen word

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_choice:
            display[position] = letter 

#Check if user is wrong.
    if user_choice not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.") 

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win")
        
#Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])  