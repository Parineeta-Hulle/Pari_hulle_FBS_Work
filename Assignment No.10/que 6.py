numbers = [12, 34, 56, 12, 34, 78, 56]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)