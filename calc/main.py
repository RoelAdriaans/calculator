from math import prod


def add(*args):
    return sum(args)


def mult(*args: float | int) -> float | int:
    """Multiply a list of numbers together
    Args:
        *args (float | int): A list of numbers to multiply
    Returns:
        float | int: The product of the numbers
    """
    return prod(args)


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {mult(2, 3)}")
