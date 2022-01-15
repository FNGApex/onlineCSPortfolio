from math import sqrt, floor
n = int(input())
if n == 1:
  print(1)
elif n == 0:
  print(10)
else:
  factors = []
  run = True
  ans = -1
  while (run):
    rootn = floor(sqrt(n))
    for i in range(9,1,-1):
      if n % i == 0: 
        factors.append(i)
        n = n//i
        ans = 1
        if i > 9: 
          ans = -1
          run = False
        break
    else:
      break

  # Last Factor Check
  if n > 9:
    ans = -1
  elif n == 1:
    n = 0
  else:
    factors.append(n)

#Sorting Answers
  if ans == -1:
    print(ans)
  else:
    ans = ""
    factors = sorted(factors)
    for i in factors:
      ans += str(i)
    print(ans)
  #