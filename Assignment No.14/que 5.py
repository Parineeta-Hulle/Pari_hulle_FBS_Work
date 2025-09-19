strings = ["flower", "flow", "flight"]

if not strings:
    print("No strings provided")
else:

    prefix = strings[0]

    for s in strings[1:]:

        while prefix and not s.startswith(prefix):
            prefix = prefix[:-1]

    print("Longest common prefix:", prefix)
