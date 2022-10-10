startingyear = int(input())
endingyear = int(input())
print("All positions change in year",startingyear)
while True:
    if (endingyear) >= (startingyear + 60):
        print("All positions change in year",(startingyear + 60))
        startingyear += 60
    else:
        break