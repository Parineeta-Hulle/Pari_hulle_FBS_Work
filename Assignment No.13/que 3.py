my_dict = {'name': 'Alice', 'age': 25, 'city': 'Pune'}
key = input("Enter the key to check: ")

if key in my_dict:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")