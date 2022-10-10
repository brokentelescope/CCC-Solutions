howManyStudents = int(input())
firstList = input().split()
secondList = input().split()
partners = []
if howManyStudents % 2 == 0:
    for x in range(len(firstList)):
        i = []
        i.append(firstList[x])
        i.append(secondList[x])
        i.sort()
        if i in partners:
            pass
        else:
            partners.append(i)
    if len(partners) == howManyStudents / 2:
        print("good")
    else:
        print("bad")
else:
    print("bad")