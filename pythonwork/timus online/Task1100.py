amount_of_teams = int(input())
teams = []
for i in range(amount_of_teams):
    teams.append((input().split()))
i = 0
while True:
    if i == len(teams)-1:
        break
    if teams[i][1] < teams[i+1][1]:
        teams[i], teams[i+1] = teams[i+1], teams[i]
        i = 0
        continue
    i += 1
for i in teams:
    print(*teams[i])
