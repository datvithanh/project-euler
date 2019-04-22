
grid = [[0]*22 for _ in range(22)]

grid[1][1] = 1

for i in range(1,22):
    for j in range(1,22):
        if i == 1 and j == 1:
            continue
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[21][21])