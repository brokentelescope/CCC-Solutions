n = int(input())
k = int(input())

visited = {}


def tryNext(x, y):
    if x == 0 or y == 1:
        return 1
    result = 0
    for i in range(0, x // y + 1):
        if (x - i * y, y - 1) not in visited:
            visited[(x - i * y, y - 1)] = tryNext(x - i * y, y - 1)
        result += visited[(x - i * y, y - 1)]
    return result


print(tryNext(n - k, k))
