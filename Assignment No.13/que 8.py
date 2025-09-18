text = input("Enter a string: ")

words = text.lower().split()


word_freq = {}


for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


print("Word frequencies:", word_freq)
