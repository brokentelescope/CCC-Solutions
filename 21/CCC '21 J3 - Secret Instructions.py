last = "a"
while True:
    num = input()
    if num == "99999":
        break
    else:
        
        if (int(num[0]) + int(num[1])) % 2 == 0:
            if int(num[0]) + int(num[1]) == 0:
                print(last + num[2] + num[3] + num[4])
            else:
                print("right " + num[2] + num[3] + num[4])
                last = "right "
        else:
            print("left " + num[2] + num[3] + num[4])
            last = "left "
