import random

MIN_NUMBER = 1
MAX_NUMBER = 10

secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

while True:
    guess = int(input(f"Guess number from {MIN_NUMBER} and {MAX_NUMBER} :"))
    
    if guess == secret_number:
       print("You Guessed The Right Number")
       break

    elif guess < secret_number :
        print("The Guess Is too Low")
    else:
        print("The Guess Is Too High. Try Again")