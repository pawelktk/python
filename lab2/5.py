def transposition_cipher(text: str, key: int) -> str:
    if key > len(text) or key <= 0:
        return text

    text_list = list(text)
    for i in range(0, len(text) - key, key):
        text_list[i], text_list[i + key] = text_list[i + key], text_list[i]
    return "".join(text_list)


print(transposition_cipher("abcdefgh", 2))
