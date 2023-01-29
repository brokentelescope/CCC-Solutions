n = int(input())

def factor(n):
    # find largest factor
    x = n-1

    while x >= int(n ** 0.5) and x > 1:
        if n % x == 0: 
            return x 
        else:
            x -= 1

    # if its prime return a big number
    return int(5e6+1)


cost = 0

while n != 1:
    f = factor(n)

    # if f is prime, we can only subtract by one for the cost of n-1

    if f >= n:
        n -= 1
        cost += n 

    # otherwise subtract by largest factor for a cost of n/f
    else:
        n -= f 
        cost += n//f

print(cost)