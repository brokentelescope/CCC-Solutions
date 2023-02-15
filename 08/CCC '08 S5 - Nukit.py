n = int(input())

# memoization 
# there is a total of 30*30*30*30 = 810000 combinations of A, B, C, and D atoms
# keep the result of every combination you solve and access it from the dictionary 

lose_dp = {}
win_dp = {}

def AABDD(a, b, c, d):
    return a >= 2 and b >= 1 and c >= 0 and d >= 2

def ABCD(a, b, c, d):
    return a >= 1 and b >= 1 and c >= 1 and d >= 1

def CCD(a, b, c, d):
    return a >= 0 and b >= 0 and c >= 2 and d >= 1

def BBB(a, b, c, d):
    return a >= 0 and b >= 3 and c >= 0 and d >= 0 

def AD(a, b, c, d):
    return a >= 1 and b >= 0 and c >= 0 and d >= 1

def Move(a, b, c, d):
    return AABDD(a,b,c,d) or ABCD(a,b,c,d) or CCD(a,b,c,d) or BBB(a,b,c,d) or AD(a,b,c,d)

# if you can't move or all your moves lead into a win on the next move, you lose
def lose(a, b, c, d):

    if (a,b,c,d) in lose_dp:
        return lose_dp[(a,b,c,d)]

    if not Move(a,b,c,d):
        lose_dp[(a,b,c,d)] = True
        return True 

    if AABDD(a, b, c, d):
        if not win(a-2, b-1, c-0, d-2):
            lose_dp[(a,b,c,d)] = False
            return False 
    if ABCD(a, b, c, d):
        if not win(a-1, b-1, c-1, d-1):
            lose_dp[(a,b,c,d)] = False
            return False 
    if CCD(a, b, c, d):
        if not win(a-0, b-0, c-2, d-1):
            lose_dp[(a,b,c,d)] = False
            return False 
    if BBB(a, b, c, d):
        if not win(a-0, b-3, c-0, d-0):
            lose_dp[(a,b,c,d)] = False
            return False 
    if AD(a, b, c, d):
        if not win(a-1, b-0, c-0, d-1):
            lose_dp[(a,b,c,d)] = False
            return False 
    lose_dp[(a,b,c,d)] = True
    return True

# if any of your moves force a loss for the next move, you win
def win(a, b, c, d):
    if (a,b,c,d) in win_dp:
        return win_dp[(a,b,c,d)]

    if AABDD(a, b, c, d):
        if lose(a-2, b-1, c-0, d-2):
            win_dp[(a,b,c,d)] = True
            return True
    if ABCD(a, b, c, d):
        if lose(a-1, b-1, c-1, d-1):
            win_dp[(a,b,c,d)] = True
            return True    
    if CCD(a, b, c, d):
        if lose(a-0, b-0, c-2, d-1):
            win_dp[(a,b,c,d)] = True
            return True 
    if BBB(a, b, c, d):
        if lose(a-0, b-3, c-0, d-0):
            win_dp[(a,b,c,d)] = True
            return True 
    if AD(a, b, c, d):
        if lose(a-1, b-0, c-0, d-1):
            win_dp[(a,b,c,d)] = True
            return True 
    win_dp[(a,b,c,d)] = False
    return False

for x in range(n):
    a, b, c, d = [int(x) for x in input().split()] 
    if win(a,b,c,d):
        print("Patrick")
    else:
        print("Roland")