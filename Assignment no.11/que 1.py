numbers = [12, 7, 9, 4, 10, 5, 8]


even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)