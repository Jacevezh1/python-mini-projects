from posixpath import join
import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_words(words) # Letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) # What the user has guessed
    used_letters = set() # What the user has guessed
    lives = 3
    
    # Getting user input
    while len(word_letters) > 0 and lives > 0: 

        # Letters used
        print('You have', lives, 'lives left and you have used this letters', ' '.join(used_letters))

        # What current words is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' ',join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #take away life if wrong
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You already guessed that letter')

        else:
            print('You didnt input a valid letter')

        if lives == 0:
            print('You died, sorry. The word was', word)
        else:
            print('You guessed the word', word, '!!')




if __name__ == '__main__':
    hangman()