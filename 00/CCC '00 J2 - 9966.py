bad = "23457"
counter = 0

start = int(input())
stop = int(input())

for x in range(start,stop+1):

    string = str(x)
    new = ""
    check = True

    for y in string:
        if y in bad:
            check = False
    
    if check:
        for y in string:
            if y == "6":
                new += "9"
            elif y == "9":
                new += "6"
            else:
                new += y
    
    if new[::-1] == string:
        counter += 1
        # print(new)

print(counter)
