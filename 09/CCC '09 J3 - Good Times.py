time = input()
time = "0"*(4-len(time)) + time
hrs = int(time[:2])
mins = int(time[2:])

eastern = hrs*60+mins 
pacific = eastern-180
mountain = eastern-120
central = eastern-60
atlantic = eastern+60
newfoundland = eastern+90 

def solve(total):
    total %= 1440 
    hrs = total//60
    mins = total % 60
    if hrs == 0: hrs = ""
    return str(hrs) + str(mins)+"0"*(2-len(str(mins)))

print(f"{solve(eastern)} in Ottawa")
print(f"{solve(pacific)} in Victoria")
print(f"{solve(mountain)} in Edmonton")
print(f"{solve(central)} in Winnipeg")
print(f"{solve(eastern)} in Toronto")
print(f"{solve(atlantic)} in Halifax")
print(f"{solve(newfoundland)} in St. John's")
