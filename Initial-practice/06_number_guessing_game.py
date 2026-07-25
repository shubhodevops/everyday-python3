import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)

    
print(f"\nNew Game! You have to guess the number (1-100).")
# INNER LOOP: Handles the current game guesses
while True:
    guess = int(input("Enter your guess: "))
        

        
    # CONDITIONAL LOGIC: Check the guess
    if guess < secret_number:
        print(f"Too low!")
    elif guess > secret_number:
        print(f"Too high!")
    else:
        print(f"Correct! You won the game!")
            
