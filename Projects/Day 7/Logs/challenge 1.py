#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess =input("Guess a letter: ")
user_guess.lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for guess in random_word:
  if guess == user_guess:
    print(f"correct   :{guess}")
  else:
    print(f"Incorrect :{guess}")
