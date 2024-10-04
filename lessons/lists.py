"""Basic syntax of lists"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# add an item to the list
my_numbers.append(1.5)

# create an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
game_points[2]
last_game: int = game_points[2]

# modifying by index (because lists are mutable)
game_points[1] = 72

# get length of list
len(game_points)
y: int = len(game_points)

# remove items from list
game_points.pop(1)  # index of item removed

# Write a function called display
# Input: list[int]
# RV: None
# Loop over the input and print every value
# Try calling it on game_points


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
