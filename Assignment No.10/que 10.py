numbers = [12, 34, 56, 12, 78, 12, 90]

element = int(input("Enter the element to remove: "))


numbers = [num for num in numbers if num != element]

print("List after removing", element, ":", numbers)