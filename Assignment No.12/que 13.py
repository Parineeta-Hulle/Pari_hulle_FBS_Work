
text = input("Enter a string: ")

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)