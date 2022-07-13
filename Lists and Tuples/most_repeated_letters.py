from collections import Counter

words = ["this", "is", "a", "test", "progrram"]

def most_repeating_word(words):
    word_counts = {word : max(Counter(word).items(),
                              key=lambda t: t[1]) for word in words}
    print(word_counts)
    return max(word_counts, key=lambda w: word_counts[w][1] )

print(most_repeating_word(words))
