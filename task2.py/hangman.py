import random

words = ["python", "developer", "scraper", "hangman", "internship", "programming", "java", "develop", "internet", "computer", "variable", "function", "dictionary", "algorithm", "loop", "compiler", "software"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", " ".join(used_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
