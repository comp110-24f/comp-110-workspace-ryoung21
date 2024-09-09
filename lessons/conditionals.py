"""Practicing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve is. :)"


def check_first_letter(word: str, letter: str) -> str:
    """Returns match! if the first character of word is letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))
