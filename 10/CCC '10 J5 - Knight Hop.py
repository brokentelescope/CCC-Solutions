x_moves = [2, 2, -2, -2, 1, 1, -1, -1]
y_moves = [1, -1, 1, -1, 2, -2, 2, -2]

start = [int(x) for x in input().split(" ")]
end = [int(x) for x in input().split(" ")]

possible_moves = [start]
grid = []

for i in range(8):
    grid.append([99]*8)
grid[start[0] - 1][start[1] - 1] = 0

while len(possible_moves) > 0:
    x = possible_moves[-1][0]
    y = possible_moves[-1][1]
    # if [x,y] == end:
        # break

    possible_moves.pop()

    for i in range(8):
        if 0 < x + x_moves[i] < 9 and 0 < y + y_moves[i] < 9 and grid[x-1][y-1] + 1 < grid[x + x_moves[i]-1][y + y_moves[i]-1]:
            possible_moves.append([x + x_moves[i], y + y_moves[i]])
            grid[x + x_moves[i]-1][y + y_moves[i]-1] = grid[x-1][y-1] + 1
    
print(grid[end[0]-1][end[1]-1])

# for x in grid:
#     print(x)