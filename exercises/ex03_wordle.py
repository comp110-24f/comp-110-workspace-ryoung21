"""EX03 - Wordle"""

__author__ = "730461441"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        user_guess: str = input_guess(5)
        print(f"=== Turn {turn}/6 ===")
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print(f"You won in {turn}/6 turns!")
            exit()
        if turn == 6 and user_guess != secret:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


def input_guess(secret_word_len: int) -> str:
    """Takes input guess of a word of a certain length, prompts user to input again if length incorrect"""
    secret_word_guess = input(f"Enter a {secret_word_len} character word: ")
    while len(secret_word_guess) != secret_word_len:
        secret_word_guess = input(f"That wasn't {secret_word_len} chars! Try again.")
    return secret_word_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Tests each index of secret_word to see if it matches secret_character and returns True or False."""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
        index += 1
    return False


def emojified(word_guess: str, sec_word: str) -> str:
    """Compares each index of word_guess to each index of sec_word and returns string of emojis"""
    assert len(word_guess) == len(sec_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""
    while index < len(sec_word):
        if word_guess[index] == sec_word[index]:
            emoji += GREEN_BOX
        elif contains_char(sec_word, word_guess[index]) == True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


if __name__ == "__main__":
    main(secret="codes")
