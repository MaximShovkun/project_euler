grid = []
gridSize = 20

for i in range(gridSize + 1):
    grid.append([])
    for j in range(gridSize + 1):
        grid[i].append(1)

for i in range(gridSize - 1, -1, -1):
    for j in range(gridSize - 1, -1, -1):
        grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

print('Number of routes -> {}'.format(grid[0][0]))