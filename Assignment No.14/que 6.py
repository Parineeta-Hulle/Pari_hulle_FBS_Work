numbers = [3, 5, -2, 8, -7, 4]

numbers = list(set(numbers))

max_product = numbers[0] * numbers[1]
pair = (numbers[0], numbers[1])

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] * numbers[j] > max_product:
            max_product = numbers[i] * numbers[j]
            pair = (numbers[i], numbers[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_product)
