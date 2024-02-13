from math import prod


def add(*args):
    return sum(args)


def sub(a, b):
    return a - b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {sub(5, 2)}")
