import random

words = ["python", "java", "ruby", "javascript", "html", "css", "php"]

secret_word = random.choice(words)

guessed_letters = []

while True:
    current_state = ""
    for letter in secret_word:
        if letter in guessed_letters:
            current_state += letter
        else:
            current_state += "_"
    print(current_state)

    if "_" not in current_state:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ")

    if guess in guessed_letters:
        print("You already guessed that letter. Guess again.")

    elif guess in secret_word:
        print("Good guess! Keep going.")
        guessed_letters.append(guess)

    else:
        print("Sorry, that letter is not in the word. Guess again.")
        guessed_letters.append(guess)
