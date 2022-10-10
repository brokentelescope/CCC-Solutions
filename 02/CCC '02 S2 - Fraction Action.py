numerator = int(input())
denominator = int(input())
remainder = numerator % denominator
def hcfnaive(remainder,denominator): 
    if(denominator==0): 
        return remainder 
    else: 
        return hcfnaive(denominator,remainder%denominator) 
import math 
gcd = hcfnaive(remainder, denominator)
if remainder == 0:
    print(int(numerator/denominator))
else:
    first = math.floor(numerator/denominator)
    if first != 0 and remainder%denominator != 0:
        print(first," ", int(remainder/gcd),"/",int(denominator/gcd),sep='')
    elif first == 0 and remainder%denominator != 0:
        print(int(remainder/gcd),"/",int(denominator/gcd),sep='')
    elif first ==0 and remainder%denominator == 0:
        print(int(remainder/gcd),"/",int(denominator/gcd),sep='')