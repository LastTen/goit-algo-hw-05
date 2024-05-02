from typing import Callable


def generator_numbers(text: str):
    """
    This function takes a string and returns a generator of numbers from the string.
    """
    for char in text.split(" "):
        try:
            if float(char):
                yield (float(char))
        except ValueError:
            continue


def sum_profit(text: str, func: Callable):
    """
    This function takes a string and a generator function and returns the sum of the numbers generated by the generator function.
    """
    return sum(func(text))


if __name__ == "__main__":

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    # text = "Загальний дохід працівника складається з декількох частин: 0000.00 як основний дохід, доповнений додатковими надходженнями 00 і 0 доларів."
    # text = ""
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
