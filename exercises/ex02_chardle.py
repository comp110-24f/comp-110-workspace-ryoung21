"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730461441"


def main() -> None:
    contains_char(input_word(), input_letter())


def input_word() -> str:
    five_char_word: str = input("Enter a 5-character word: ")
    if len(five_char_word) == 5:  # to check that character entered is 5 characters
        return five_char_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    character: str = input("Enter a single character: ")
    if len(character) == 1:
        return character
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(
        word
    ):  # to repeat loop until all indexes of word have been examined
        if letter == word[index]:
            print(letter + " found at index", index)
            count += 1
        index += 1
    if count == 1:  # use if, elif, else to print count number with correct tenses
        print(count, "instance of " + letter + " found in " + word)
    elif count > 1:
        print(count, "instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
