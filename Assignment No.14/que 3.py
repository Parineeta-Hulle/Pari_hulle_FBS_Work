strings = ["apple banana apple", "banana orange", "apple orange banana"]

words = []
for s in strings:
    words.extend(s.split())

unique_words = set(words)


for word in unique_words:
    count = words.count(word)
    print(f"'{word}': {count}")
