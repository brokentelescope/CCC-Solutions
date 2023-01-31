def solve(diff):
    # test all pattern lengths 

    for x in range(1, n):
        works = True
        for y in range(n-1):
            if diff[y] != diff[y%x]:
                works = False 
                break 
        if works:
            return x 
    return 0
    
while True:
    line = input()

    if line == "0":
        break 

    line = line.split()

    n = int(line[0])

    nums = [int(x) for x in line[1:]]

    diff = []

    for x in range(n-1):
        diff.append(nums[x+1]-nums[x])

    print(solve(diff))

    