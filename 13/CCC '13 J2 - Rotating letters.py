letters = "IOSHZXN"
check = True

for x in input():
    if x in letters:
        pass
    else:
        check = False
        break

if check:
    print("YES")

else:
    print("NO")


