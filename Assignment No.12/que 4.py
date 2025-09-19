
text = input("Enter a string: ")


if len(text) > 1:
    new_text = text[-1] + text[1:-1] + text[0]
else:
    new_text = text  

print("New string:", new_text)