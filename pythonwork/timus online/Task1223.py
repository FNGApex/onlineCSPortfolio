from math import log2, ceil
while True:
    x = input()
    if x == "0 0":
        break
    eggs, floors = list(map(int, x.split()))
    print(ceil(log2(floors) + 1))