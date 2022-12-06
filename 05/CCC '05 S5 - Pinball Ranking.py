import bisect
import sys 
input = sys.stdin.readline
n = int(input())

games = []
games.append(int(input()))
total = 1 

#insertion sort is jsut barely too slow 
#tle on case 9
for x in range(2,n+1):
    score = int(input())
    i = x - bisect.bisect_right(games,score)
    games.insert(bisect.bisect_right(games,score), score)
    total += i 

print(total/n)
