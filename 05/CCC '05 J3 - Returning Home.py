dirs = []
streets = ["HOME"]


while 1:
    dir = input()
    street = input()

    if street == "SCHOOL":
        dirs.append(dir)
        break
    
    dirs.append(dir)
    streets.append(street)

dirs = dirs[::-1]
streets = streets[::-1]

# print(dirs)
# print(streets)

for x in range(len(dirs)-1):
    if dirs[x] == "R":
        print(f"Turn LEFT onto {streets[x]} street.")
    else:
        print(f"Turn RIGHT onto {streets[x]} street.")

if dirs[-1] == "R":
    print("Turn LEFT into your HOME.")
else:
    print("Turn RIGHT into your HOME.")