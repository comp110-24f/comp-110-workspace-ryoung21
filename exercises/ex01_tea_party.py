"""EX01 Tea Party"""

__author__ = "730461441"


def main_planner(guests: int) -> None:
    """entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # have to change function outputs to strings when printing
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)),
        ),
    )  # have to call functions within cost function arguments


def tea_bags(people: int) -> int:
    """Returns number of guests attending tea party"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats for tea drinkers"""
    return int(
        tea_bags(people=people) * 1.5
    )  # have to set people equal to something in return statement, even if it equals itself


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and the treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
