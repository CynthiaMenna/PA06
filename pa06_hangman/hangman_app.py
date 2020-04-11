"""
   Group: Cynthia, Yessenia, Tianyi, Emily, Jessica

   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""





import random

def generate_random_word():
    words = "pencil dog house computer appreciate tablet cup glass globe monitor textbook binder feather coil meditation clip photograph frame".split()
    chosen_word = random.choice(words)
    for x in chosen_word:
        print(" _ ",end ="")
    return chosen_word


def print_word(word, guessed_letters):
    for x in word:
        if x in guessed_letters:
            print(x, end =""),
        else:
            print(" _ ", end=""),


def play_hangman():

    want_to_play = input("Do you want to play hangman? Y/N? ")

    while want_to_play == "Y" or want_to_play == "y":
        guessed_letters = []
        guesses_left = 10
        word = generate_random_word()
        letter = input("\nGuess a letter:")
        length = len(word)


        done = False
        while not done:
            if len(letter)>=2 or len(letter)==0:
                guesses_left=guesses_left - 1
                print("Please enter a single letter")
                print("\n\nThese are the letters you have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")



            elif letter in guessed_letters:  #letter has already been guessed
                guesses_left = guesses_left - 1
                print("You already guessed that letter.")
                print_word(word, guessed_letters)
                print("\n\nThese are the letters you have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")


            elif letter not in word:  #letter is not in the word
                guessed_letters.append(letter)
                print("The letter you guessed is not in the word.")
                guesses_left = guesses_left - 1
                print_word(word,guessed_letters)
                print("\n\nThese are the letters you have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")


            else:
                guessed_letters.append(letter)  #letter is in the word
                length = length-1 #number of letters left unguessed
                print("The letter is in the word.")
                print_word(word, guessed_letters)
                print("\n\nThese are the letters you have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")


            if length == 0:  #there are no more letters left to guess
                done=True
                print("\n\nYou won! The word was", word,".")
            elif guesses_left==0:  #ran out of guesses
                done=True
                print("\n\nYou lost! The word was", word,".")

            else:
                letter = input("\nGuess a letter: ")
        want_to_play = input("Do you want to play again? (Y/N)")

    print("Thanks for playing! Goodbye!")

if __name__ == '__main__':
    play_hangman()
