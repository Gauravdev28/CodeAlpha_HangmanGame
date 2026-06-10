import random

words = [
    "python",
    "github",
    "coding",
    "student",
    "laptop",
    "machine",
    "programming"
]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 50)
print("🎮 WELCOME TO HANGMAN GAME")
print("=" * 50)

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print(f"Attempts Left: {max_wrong_guesses - wrong_guesses}")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)

print("\nThanks for playing!")