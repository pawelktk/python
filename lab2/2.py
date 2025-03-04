def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    return [
        num // 10 * 10 if num < threshold else (num // 10 + 1) * 10 for num in numbers
    ]


print(round_numbers([2, 5, 10, 12, 15, 17], 10))
