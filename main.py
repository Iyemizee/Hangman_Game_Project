import random
import hangman_words
import hangman_art

stages = hangman_art.stages

print(hangman_art.logo)

word_list = hangman_words.word_list
'''randomly choose a word from the word list'''
chosen_word = random.choice(word_list)
print(chosen_word)

'''create an empty list called display based on the number of word characters'''
display = []
for char in chosen_word:
    display.append("_")
print(display)
'''ask a user to guess a letter and assign their answer to a variable called guess'''
filled_up = False
lives = 6
while not filled_up:
    guess = input("Guess a letter: ").lower()
    '''check if the guessed letter is in the chosen word and reveal the letter in the display'''
    if guess in display:
        print(f"You have already guessed {guess}")
    for index, char in enumerate(chosen_word):
        if guess == char:
            display[index] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word, you lose a life.")
        if lives == 0:
            filled_up = True
            print("You lose!")
    print(display)
    if "_" not in display:
        filled_up = True
        print("You win!!")
    print(stages[lives])
