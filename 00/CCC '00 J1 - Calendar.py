d, n = [int(x) for x in input().split()]
print("Sun Mon Tue Wed Thr Fri Sat")
print(" ".join(["   "] * (d-1)), end = " " * int(d != 1))
print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(1, 9-d)]))
print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(9-d, 16-d)]))
print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(16-d, 23-d)]))
print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(23-d, 30-d)]))
if n != 28 or d != 1:
  print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(30-d, min(n+1, 37-d))]))
  if (d, n) in [(7, 31), (7, 30), (6, 31)]: 
    print(" ".join([" " * (3-len(str(x))) + str(x) for x in range(37-d, n+1)]))
