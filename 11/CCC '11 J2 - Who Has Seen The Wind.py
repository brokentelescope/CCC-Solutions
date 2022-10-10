h = int(input())
t = int(input())

if (-6*t**4 + h*t**3 + 2 * t**2 + t) > 0:
    print("The balloon does not touch ground in the given time.")

else:
    for x in range(t):
        if (-6*x**4 + h*x**3 + 2*x**2 + x) < 0:
            print("The balloon first touches ground at hour:")
            print(x)
            break