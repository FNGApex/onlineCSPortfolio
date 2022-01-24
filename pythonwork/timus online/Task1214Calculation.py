import math
from re import L
def scramble(x: int, y: int):
    if x > 0 and y > 0:
        for i in range(x + y):
            y = x * x + y
            x = x * x + y
            y = math.floor(math.sqrt(x + y / abs(y) * -abs(y)))
            for j in range(2 * y):
                x -= y
    return (x, y)
for i in range(10):
    for j in range(10):
        print(i,j, "=>", scramble(i,j))