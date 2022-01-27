testLine = input() 
leastAmountOfEdits = 2000
debug = []
requestedLine = "Sandro"
for i in range(len(testLine)-5):
  amountOfEdits = 0
  letters = list(testLine[i:i+6])
  for j in letters[1:6]:
    if j.isupper():
      amountOfEdits += 1
  if letters[0] == "s":
    amountOfEdits += 1
  elif letters[0] != "S":
    amountOfEdits += 2
  for i in range(1,6):
    if letters[i] != requestedLine[i] and letters[i] != requestedLine[i].upper():
      amountOfEdits += 1
  if amountOfEdits < leastAmountOfEdits:
    leastAmountOfEdits = amountOfEdits
print(leastAmountOfEdits*5)