"""coordinates"""

__author__ = "730461441"


def get_coords(xs: str, ys: str) -> None:
    coords: str = ""
    index1: int = 0
    while index1 < len(xs):  # outer loop
        x_coord: str = xs[index1]
        index1 += 1
        index2: int = 0
        while index2 < len(ys):  # inner loop
            y_coord: str = ys[index2]
            coords = "(" + x_coord + "," + y_coord + ")"
            index2 += 1
            print(coords)


if __name__ == "__main__":
    print(get_coords("12", "34"))
