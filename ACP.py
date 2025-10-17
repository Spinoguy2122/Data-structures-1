import random

def guess_the_number():
    
    secret_number = random.randint(1, 100)  
    guesses_left = 6  

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue  

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {7 - guesses_left + 1} guesses!")
            return  

        guesses_left -= 1

    print(f"You ran out of guesses. The number was {secret_number}.")


guess_the_number()
