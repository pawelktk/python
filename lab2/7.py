def most_frequent_element(data: list):
    return max(set(data), key=data.count)


print(most_frequent_element([1, 2, 3, 4, 5, 1]))
