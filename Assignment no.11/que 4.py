numbers = [12, 45, 23, 67, 34]


n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  # Swap


second_largest = numbers[-2]

print("Sorted list:", numbers)
print("Second largest element:", second_largest)