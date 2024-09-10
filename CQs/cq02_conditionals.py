"""CQ02"""

__author__ = "730461441"


def guess_a_number(
    secret: int, guess: int
) -> None:  # must put the guess in parameters to store response
    secret = 7
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    else:
        if guess < secret:
            print("Your guess was too low! The secret number is " + str(secret))
        if guess > secret:
            print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number(secret=int, guess=int(input("Guess a number.")))
