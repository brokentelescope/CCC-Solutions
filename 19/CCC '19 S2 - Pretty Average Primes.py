import math

hm_nums = int(input())

def prime(number):
    for x in range(2, int(math.sqrt(number)+1)):
        if number % x == 0:
            return False
    
    return True
    
for x in range(hm_nums):
    avg = int(input())
    
    for x in range(3, avg*2, 2):
        if prime(x):
            if prime(avg*2-x):
                print(str(x) + " " + str(avg*2-x))
                break
    
