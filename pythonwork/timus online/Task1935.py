# i[j] = a[i]
n = int(input())
wingsAmount = list(map(int, input().split()))
print(sum(wingsAmount)+max(wingsAmount))