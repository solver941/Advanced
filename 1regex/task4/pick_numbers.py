import re


def pick_numbers(text: str) -> list[int]:
    text = text.replace(" ", "")
    numbers = re.split(r'\D+', text)
    int_numbers = [int(number) for number in numbers if number]
    return int_numbers
