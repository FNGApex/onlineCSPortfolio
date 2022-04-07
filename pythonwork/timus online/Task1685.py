def un_scramble(part: list):
    if len(part) < 2:
        return part
    return un_scramble(part[1:((len(part)-1)//2)+1]) + [part[0]] + un_scramble(part[(len(part)-1)//2+1:])

print(*un_scramble([i for i in input()]), sep="")
