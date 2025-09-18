board = []

for i in range(10):  
    row = []
    for j in range(100 - i*10, 100 - i*10 - 10, -1):  
        row.append(j)
    if i % 2 != 0:  
        row.reverse()
    board.append(row)


for row in board:
    print(' '.join(f"{num:3}" for num in row))