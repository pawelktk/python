from collections import defaultdict


def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    word_dict = defaultdict(list)
    for word in words:
        word_dict[len(word)].append(word)
    return dict(word_dict)


words_list = ["a", "b", "c", "aa", "bb", "aaa"]
print(group_words_by_length(words_list))
