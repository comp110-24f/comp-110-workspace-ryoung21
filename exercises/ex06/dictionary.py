"""EX06 - dictionary"""

__author__ = "730461441"


def invert(dict_to_invert: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dict."""
    inverted: dict[str, str] = {}  # Create empty dict to store inverted values

    for key in dict_to_invert:
        value = dict_to_invert[key]

        if value in inverted:  # Check if key in inverted equals value in original
            raise KeyError("KeyError")

        inverted[value] = key

    return inverted


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently in names_and_colors."""
    color_occurences: dict[str, int] = {}  # Store color counts
    first_occurence: dict[str, int] = {}  # Store the index of first occurrence
    index: int = 0

    for name in names_and_colors:
        color = names_and_colors[name]

        # Count occurrences of each color
        if color in color_occurences:
            color_occurences[color] += 1
        else:
            color_occurences[color] = 1
            first_occurence[color] = index
            index += 1

    most_frequent_color: str = ""
    max_count: int = 0

    # Determine most frequent color
    for color in color_occurences:
        count = color_occurences[color]
        # Update  most frequent color
        if count > max_count or (
            count == max_count
            and first_occurence[color] < first_occurence[most_frequent_color]
        ):
            most_frequent_color = color
            max_count = count

    return most_frequent_color


def count(strings: list[str]) -> dict[str, int]:
    """Produces a dict where each key is a unique value and each value is the frequency of strings."""
    counted: dict[str, int] = {}  # empty dict to store counts of values in .
    for elem in values:
        if elem in counted:  # Check if item is already a key
            counted[elem] += 1
        else:
            counted[elem] = 1  # Start counting for new keys
    return counted


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sorts words into a dict based on the letter they start with."""
    end_dictionary: dict[str, list[str]] = (
        {}
    )  # empty dict to store resulting keys and values

    for word in words:
        first_letter = word[0].lower()  # make sure letter is lowercase

        if first_letter not in end_dictionary:
            end_dictionary[first_letter] = []

        end_dictionary[first_letter].append(word)  # add word to growing list value

    return end_dictionary


def update_attendance(
    attendance: dict[str, list[str]], day_of_week: str, student: str
) -> None:
    """Function mutates dictionary according to actual student attendance log."""
    if day_of_week not in attendance:
        attendance[day_of_week] = (
            []
        )  # must start a new list if the day is not the same to avoid KeyError
    attendance[day_of_week].append(student)

    return None
