import sys
input = sys.stdin.readline

hm_readings = int(input())

readings = [0] * 1000
for x in range(hm_readings):
    reading = -int(input())
    readings[reading] += 1

max_reading = readings.index(max(readings))

readings[max_reading] = 0

second = []
second_reading = max(readings)

for x in range(1000):
    if readings[x] == second_reading:
        second.append(x)

print(
    max(
        abs(max_reading-max(second)),abs(max_reading-min(second))
    )
    )

