from math import floor
counter = 0


def scramble(part: list):
    global counter
    counter += 1
    if len(part) <= 2:
        return part
    return ([part[(
        len(part)-1)//2]] + scramble(part[:(len(part)-1)//2]) + scramble(part[(len(part)-1)//2+1:]))


for x in [1, 12, 123, 1234, 12345, 123456, 125678, 123456789, 1234567890]:
    counter = 0
    un_scramble = [i for i in str(x)]
    size = len(un_scramble)
    middle = (len(un_scramble)-1)//2
    print()
    print(x)
    print(*scramble(un_scramble), sep="")
    print(counter)
    print(round(len(str(x))/2))
    print()
