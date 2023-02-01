def solve(m, x, y):
    size = 5 ** (m-1)
    curx, cury = x//size, y//size

    # 0 0 0 0 0
    # 0 0 0 0 0 
    # 0 0 y 0 0 
    # 0 y x y 0
    # 0 x x x 0

    # if it is in the spots marked by x, it is guaranteed crystal

    if (cury == 0 and curx in [1, 2, 3]) or (curx == 2 and cury == 1):
        return "crystal"
    
    # if it is in the spots marked by 0, it is guaranteed to be empty

    if curx in [0, 4] or cury in [3, 4] or (curx == 1 and cury == 2) or (curx == 3 and cury == 2):
        return "empty"

    # if it is in the spots marked by y, we aren't sure

    if (curx in [1, 3] and cury == 1) or (curx == 2 and cury == 2):
        # if its magnification level 1, we know that they are empty
        if m == 1:
            return "empty"
        # otherwise go to the prior level
        return solve(m-1, x % size, y % size)

for x in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    print(solve(a, b, c))