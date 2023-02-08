line = input()
h = line.count("H")
v = line.count("V")

h  = h % 2 
v = v % 2

if h == 0 and v == 0:
    print("1 2")
    print("3 4")

elif h == 1 and v == 0:
    print("3 4")
    print("1 2")

elif h == 0 and v == 1:
    print("2 1")
    print("4 3")

else:
    print("4 3")
    print("2 1")