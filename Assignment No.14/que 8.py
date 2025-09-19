strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in strings:
    key = ''.join(sorted(word))
    anagrams[key] = anagrams.get(key, []) + [word]

for group in anagrams.values():
    print(group)
