quarters = int(input())
first = int(input())
second = int(input())
third = int(input())
plays = 0
while quarters > 0:

    plays += 1
    first += 1
    if first == 35:
        quarters += 30
        first = 0
    quarters -= 1

    if quarters > 0:
        plays += 1
        second += 1
        if second == 100:
            quarters += 60
            second = 0
        quarters -= 1
    else:
        break

    if quarters > 0:
        plays += 1
        third += 1
        if third == 10:
            quarters += 9
            third = 0
        quarters -= 1
    else:
        break

print(f"Martha plays {plays} times before going broke.")
