import random

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)

lives = 6
guessed_letters = []

print("Welcome to Hangman!")

while "_" in display and lives > 0:
    print("\n" + " ".join(display))
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue
        
    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"Incorrect! You have {lives} lives left.")

if "_" not in display:
    print("\n" + " ".join(display))
    print("Congratulations! You guessed the word!")
else:
    print(f"\nYou ran out of lives! The word was: {chosen_word}")