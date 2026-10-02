import random

def get_valid_number(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Select difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            lower, upper = 1, 50
            max_attempts = 10
            break
        elif choice == "2":
            lower, upper = 1, 100
            max_attempts = 12
            break
        elif choice == "3":
            lower, upper = 1, 500
            max_attempts = 15
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    secret_number = random.randint(lower, upper)
    attempts = 0

    while attempts < max_attempts:
        guess = get_valid_number(f"Guess the number between {lower} and {upper}: ", lower, upper)
        attempts += 1

        if guess < secret_number:
            print("Higher number please 👆🔼")
        elif guess > secret_number:
            print("Lower number please 👇🔽")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts 👍✅")
            break
    else:
        print(f"Sorry! You ran out of attempts. The number was {secret_number}.")

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            play_game()
            return
        elif play_again in ["no", "n"]:
            print("Thanks for playing!")
            return
        else:
            print("Please answer with yes or no.")

play_game()

