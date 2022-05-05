n, m, y = list(map(int, input().split()))
answer = [x for x in range(0, m) if x**n % m == y]
if answer == []:
    print(-1)
else:
    print(*answer)
