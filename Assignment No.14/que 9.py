numbers = [1, 2, 3, 4, 5, 6]
target = 10
triplets = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                triplet = [numbers[i], numbers[j], numbers[k]]
                triplet.sort()
                if triplet not in triplets:
                    triplets.append(triplet)

print("Unique triplets with sum", target, ":", triplets)
