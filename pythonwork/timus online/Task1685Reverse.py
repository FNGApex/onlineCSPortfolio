from math import floor


def scramble(part: list,  mode: bool = "Whole"):
    if mode == "Left":
        return part
    if mode == "Right":
        return part


un_scramble = [i for i in "1234567890ABCDEFG"]
size = len(un_scramble)
middle = (len(un_scramble)-1)//2
print(scramble(un_scramble[:(len(un_scramble)-1)//2], mode="Left") + [un_scramble[(
    len(un_scramble)-1)//2]] + scramble(un_scramble[(len(un_scramble)-1)//2+1:], mode="Right"))
# print(scramble(un_scramble))
