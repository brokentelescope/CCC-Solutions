int_1 = input().split(" ")
int_2 = input().split(" ")
hm_moves = int(input())

moves_needed = abs(int(int_1[0]) - int(int_2[0])) + abs(int(int_1[1]) - int(int_2[1]))
leftover = hm_moves - moves_needed

if leftover >= 0 and leftover % 2 == 0:
    print("Y")
else:
    print("N")