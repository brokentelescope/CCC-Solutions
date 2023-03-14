n = int(input())
k = int(input())

memo = {}

# n : slices
# k : ppl
def solve(n, k):
    if (n, k) in memo:
        return memo[(n, k)]
    
    # if # of slices < # of ppl, return 0
    # because each person must get at least one slice
    if n < k:
        return 0 
    
    # if # of slices == # of ppl or # of ppl == 1, return 1
    # if the # of slices == # of ppl, each person gets 1 slice
    # if there is only one person, that  person gets all the slices
    if n == k or k == 1:
        return 1
    
    # otherwise, we can either give each person one slice and continue
    # or we can give one person one slice and get rid of them from the line
    memo[(n,k)] = solve(n-1, k-1) + solve(n-k, k)
    return memo[(n, k)]

print(solve(n, k))