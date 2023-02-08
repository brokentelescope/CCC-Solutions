x = []
x.append(input())
x.append(input())
x.append(input())
x.append(input())
x.append(input())
x.append(input())
if x.count("W") == 5 or x.count("W") == 6:
    print("1")
elif x.count("W") == 3 or x.count("W") == 4:
    print("2")
elif x.count("W") == 1 or x.count("W") == 2:
    print("3")
else:
    print("-1")