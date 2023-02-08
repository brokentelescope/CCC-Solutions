def solve(s):
    out = []
    cnt = 0 
    last = s[0]
    s += "`"
    for x in range(len(s)):
        if s[x] == last:
            cnt += 1 
        else:
            out.append(str(cnt))
            out.append(last)
            cnt = 1
            last = s[x]
    print(" ".join(out))
    
for x in range(int(input())):
    solve(input())



