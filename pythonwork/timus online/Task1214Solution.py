x, y = list(map(int, input().split()))
if x == y:
    print(x, x)
elif x < 0 or y < 0:
    print(x, y)
elif y % 2 == 1:
    if x % 2 == 1:
        print(x, y)
    else:
        print(y,x)
elif x % 2 == 1:
  print(y,x)
else:
  print(x,y)