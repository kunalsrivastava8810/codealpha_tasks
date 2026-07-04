import random


words = ["python", "school", "planet", "window", "guitar"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You can make {max_incorrect_guesses} incorrect guesses.\n")

while incorrect_guesses < max_incorrect_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
    elif guess in guessed_letters:
        print("You already guessed that letter.\n")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

if incorrect_guesses == max_incorrect_guesses:
    print("Game over! The word was:", secret_word)
