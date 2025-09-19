text = input("Enter a string: ")
n = int(input("Enter index to remove: "))

print("Result:", text[:n] + text[n+1:])