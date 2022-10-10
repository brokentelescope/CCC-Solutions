x =  1
 
while True:
  y = int(input())
  if y == 0:
    print("You Quit!")
    break
  if x + y <= 100:
    x += y
  if x == 9:
    x = 34
  if x == 40:
    x = 64
  if x == 67:
    x = 86
  if x == 54:
    x = 19
  if x == 90:
    x = 48
  if x == 99:
    x = 77
  print("You are now on square",x)
  if x == 100:
    print("You Win!")
    break