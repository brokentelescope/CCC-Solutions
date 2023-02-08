rows = []

for x in range(4):
    row = input().split(" ")
    rows.append(list(map(int, row)))

magic_true = 1
while magic_true != 8:
    magic = sum(rows[0])
    if sum(rows[1]) == magic:
        magic_true += 1
    else:
        break

    if sum(rows[2]) == magic:
       magic_true += 1
    else:
        break

    if sum(rows[3]) == magic:
        magic_true += 1
    else:
        break

    if rows[0][0] + rows[1][0] + rows[2][0] + rows[3][0] == magic:
        magic_true += 1
    else:
        break

    if rows[0][1] + rows[1][1] + rows[2][1] + rows[3][1] == magic:
        magic_true += 1
    else:
        break

    if rows[0][2] + rows[1][2] + rows[2][2] + rows[3][2] == magic:
        magic_true += 1
    else:
        break

    if rows[0][3] + rows[1][3] + rows[2][3] + rows[3][3] == magic:
        magic_true += 1
    else:
        break

if magic_true == 8:
    print("magic")
else:
    print("not magic")