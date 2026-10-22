import random


def play():
    # Outer loop: each pass is one complete game with a new secret number
    while True:
        secret = random.randint(1, 1000)  # both endpoints are inclusive
        attempts = 0  # reset the attempt counter for every new game

        # Inner loop: keep asking until the player guesses correctly or quits
        while True:
            guess = input(
                "Guess the number between 1 and 1000 "
                "(type 'bye' or 'exit' to quit): "
            ).strip().lower()

            # Quit command ends the whole program
            if guess in ("bye", "exit"):
                print("Goodbye!")
                return

            # Reject anything that isn't entirely digits (also catches empty input)
            # Invalid entries do not count as attempts
            if not guess.isdigit():
                print("Please enter a valid number")
                continue

            attempts += 1
            number = int(guess)

            if number > secret:
                print("Too high!")
            elif number < secret:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number! "
                      f"It took you {attempts} attempts.")
                break  # leave the inner loop; outer loop starts a new game


if __name__ == "__main__":
    play()