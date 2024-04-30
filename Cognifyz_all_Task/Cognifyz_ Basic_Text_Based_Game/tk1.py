import random

def guess_game():
    print("*****Welcome to the Guessing Game******")
    print("Think of a number between 1 to 50.")

    sec_num = random.randint(1, 50)

    attempt = 0
    max_attempt = 5  

    while attempt < max_attempt:
        try:
            guess = int(input("Enter your guess: "))

            if guess == sec_num:
                print("Congratulations! You won.")
                break
            else:
                print("Wrong guess. Please try again!")
                attempt += 1

        except ValueError:
            print("Invalid. Please enter a valid number.")

    else:
        print(f"Sorry, you didn't guess the number in time. The correct number was {sec_num}.")
        print("Better luck next time!")
        print("Thank you!")

if __name__ == "__main__":
    guess_game()
