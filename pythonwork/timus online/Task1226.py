from sys import stdin
textinput = stdin.readlines()
for i in textinput:
  unrefined_text = i
  if unrefined_text[-1] != '\n':
    unrefined_text += '\n'
  refined_text = []
  validation = ""
  for j in unrefined_text:
    if j.isalpha() and j != "":
      validation += j
    else:
      if validation != "":
        refined_text.append((validation,-1))
        validation = ""
      refined_text.append((j,1))
    #Validate Word
  for i in refined_text:
    print(i[0][::i[1]],end="")