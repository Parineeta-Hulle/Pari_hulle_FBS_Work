list_of_sublists = [[1, 3], [2, 1], [4, 2], [3, 5]]

list_of_sublists.sort(key=lambda x: x[1])

print("List sorted by second element:", list_of_sublists)