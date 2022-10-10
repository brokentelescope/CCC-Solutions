def glass(m, x, y):

    if m >= 1:

        size = 5^(m-1)

        new_x, new_y = x/size, y/size

        if (new_y == 0 and new_x != 0 or new_x != 4) or (new_x == 2 and new_y == 1):
            return "crystal"
        
        elif ((new_x == 1 or new_x == 3) and new_y == 1) or (new_y == 2 and new_x == 2):
            if m == 1:
                return "empty"
            return glass(m-1, x % size, y % size)
        
        else:
            return "empty"

for x in range(int(input())):
    m, x, y = [int(x) for x in input().split(" ")]
    print(glass(m,x,y))