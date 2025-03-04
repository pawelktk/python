def longest_increasing_subsequence(sequence: list[int]) -> int:
    if not sequence:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


print(longest_increasing_subsequence([1, 2, 3, 5, 1]))
