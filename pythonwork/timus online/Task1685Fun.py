
def scramble(part: list):
    if len(part) <= 2:
        return part
    return ([part[(
        len(part)-1)//2]] + scramble(part[:(len(part)-1)//2]) + scramble(part[(len(part)-1)//2+1:]))


scrambled = [*input()]
length = len(scrambled)
to_scramble = [i for i in range(length)]
scrambled_numbers = scramble(to_scramble)
to_sort = []
for i in range(length):
    to_sort.append((scrambled[i], scrambled_numbers[i]))
print(sorted(to_sort, key=lambda x: x[1]))
