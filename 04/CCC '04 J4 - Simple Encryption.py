from string import ascii_uppercase

def shift(key, let):
    key = ord(key)-65
    let = ord(let)
    if let + key > 90:
        return shift(chr(key-(90-let)+65-1), "A")
    return chr(let+key)

def stripp(string):
    g = ascii_uppercase
    new = ""
    for x in string:
        if x in g:
            new += x
    return new 

key = input(); msg = input(); key = stripp(key); msg = stripp(msg)

solve = [[] for x in range(len(key))]

cnt = 0
stop = True
while stop:
    for x in range(len(key)):
        if cnt < len(msg):
            solve[x].append(msg[cnt])
            cnt += 1
        else:
            stop = False
            break 

cnt = 0
ans = ""
stop = True
while stop:
    for x in range(len(key)):
        if cnt < len(msg):
            ans += shift(key[x], solve[x][0])
            solve[x].pop(0)
            cnt += 1
        else:
            stop = False
            break 

print(ans)

