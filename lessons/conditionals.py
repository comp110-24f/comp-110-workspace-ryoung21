"""Practicing my conditionals"""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("Have a nice day!")


print(less_than_10(num=7))
