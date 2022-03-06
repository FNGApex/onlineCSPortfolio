n = int(input())
x = str(1**n+2**n+3**n+4**n)
amountOfZeroes = 0
for i in range(len(x),0,-1):
  if x[i-1] == 0:
    amountOfZeroes += 1
print(amountOfZeroes)