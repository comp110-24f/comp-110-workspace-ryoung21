"""CQ02"""

__author__ = "730461441"


def guess_a_number() -> None:
    secret: int = 7
    x = input("Guess a number.")
    print("Your guess was ", x)
    x = int(x)
    if x == secret:  # provide response based on guess
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
