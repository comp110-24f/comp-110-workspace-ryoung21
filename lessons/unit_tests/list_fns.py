def get_first(input: list[str]) -> str:
    """Returns first element of a list."""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns and removes first element."""
    first_elem: str = input[0]
    input.pop(0)  # remove first_elem
    return first_elem
