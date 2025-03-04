import re


def count_syllables(word: str) -> int:
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev_char = False

    for char in word:
        if char in vowels:
            if not prev_char:
                count += 1
            prev_char = True
        else:
            prev_char = False

    return max(1, count)


def readability_score(text: str) -> float:
    sentences = re.split(r"[.!?]", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0.0
    words = text.split()
    num_words = len(words)
    num_sentences = len(sentences)
    num_syllables = sum(count_syllables(word) for word in words)

    avg_words_per_sentence = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words

    # Wzór Flescha: 206.835 - 1.015 * (średnia liczba słów na zdanie) - 84.6 * (średnia liczba sylab na słowo)
    score = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)

    return round(score, 2)


text1 = "This is a simple sentence. It is easy to read!"
text2 = "Complexity increases when the number of words in a sentence grows significantly, and syllables accumulate."

print(readability_score(text1))
print(readability_score(text2))
