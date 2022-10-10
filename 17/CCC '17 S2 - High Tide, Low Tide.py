hm_readings = int(input())
readings = input(). split(" ")
for i in range(hm_readings):
    readings[i] = int(readings[i])
    
readings.sort()

if hm_readings % 2 == 0:
    high = int(hm_readings/2)
    low = high - 1
else:
    low = int(hm_readings/2)
    high = low + 1

while high < hm_readings:
    print(readings[low], readings[high], end=" ")
    low -= 1
    high += 1

if hm_readings % 2 == 1:
    print(readings[0])