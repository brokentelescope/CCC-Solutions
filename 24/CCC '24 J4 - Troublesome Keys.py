# non-trivial

import string

good = input(); n = len(good)
bad = input(); m = len(bad)

alphabet = string.ascii_lowercase

# brute force all 26 letters to be the quiet key 
def solve(c):
    i = j = 0
    silly = ('', '')
    while i < n and j < m:
        if (good[i] == c): 
            i += 1
            continue 
        if good[i] != bad[j]:
            if silly[0] == '':
                silly = (good[i], bad[j])
            else:
                if (good[i], bad[j]) != silly:
                    return False 
        i += 1 
        j += 1

    # print(i, j)
    while i < n and good[i] == c: 
        i += 1
    if i == n and j == m:
        return silly
    return False

for c in alphabet:
    ret = solve(c)
    if ret:
        print(ret[0], ret[1])
        if n == m:
            print('-')
        else:
            print(c)
        break
