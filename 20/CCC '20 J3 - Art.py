num_of_dots = int(input())
dots_x = []
dots_y = []

for x in range(num_of_dots):
    dot = input().split(",")
    dots_x.append(int(dot[0]))
    dots_y.append(int(dot[1]))

print(str(min(dots_x)-1) + "," + str(min(dots_y)-1))
print(str(max(dots_x)+1) + "," + str(max(dots_y)+1))