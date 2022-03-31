from math import floor
scramble = [i for i in input()]
size = len(scramble)
original = []*size
middle = floor((size)/2)
original[0] = scramble[middle]
#gtorhoprahy
#1
# g 1 = middle or 
# t 2 = middle/2 or 
# o 3 = middle

#ortho g raphy -> g
#or t ho -> gt
for i in range(1, middle):
    