# recursive brute force solution
# basically for any hand try all possible combinations of two cards and operations
# then replace those two cards with the obtained result
# repeat until there is only one card left in the hand

def solve(hand):
    n = len(hand)
    if n == 1:
        if hand[0] <= 24:
            return hand[0]
        return 0
    maxval = 0 
    
    for x in range(n):
        for y in range(n):
            if x == y: continue
            #addition
            add = hand.copy()
            a = add.pop(x)
            b = add.pop(y-1)
            add.append(a+b)
            
            addition = solve(add)
            
            #subtract 
            sub = hand.copy()
            a = sub.pop(x)
            b = sub.pop(y-1)
            sub.append(a-b)
            
            subtraction = solve(sub)
            
            #multiply
            mult = hand.copy()
            a = mult.pop(x)
            b = mult.pop(y-1)
            mult.append(a*b)

            multiplication = solve(mult)

            
            #division 
            division = 0
            if b != 0 and a % b == 0:
                div = hand.copy()
                a = div.pop(x)
                b = div.pop(y-1)
                div.append(a//b)
                
                division = solve(div)
            
            maxval = max(maxval, addition, subtraction, multiplication, division)
    
    return maxval 
    
for x in range(int(input())):
    hand = []
    for y in range(4):
        hand.append(int(input()))
    print(solve(hand))