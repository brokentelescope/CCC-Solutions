angles = []
angles.append(int(input()))
angles.append(int(input()))
angles.append(int(input()))
if angles[0] + angles[1] + angles[2] == 180:
    if angles[0] == angles[1] and angles[1] == angles[2]:
        print("Equilateral")
    elif angles[0] != angles[1] and angles[1] != angles[2] and angles[0] != angles[2]:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")