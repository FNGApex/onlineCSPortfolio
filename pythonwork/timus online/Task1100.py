amount_of_teams = int(input())
teams = []
for i in range(amount_of_teams):
  teams.append(set(map(int,input().split())))
teams.sort(reverse=True,key=lambda x: x[1])
for i in teams:
  print(*i,sep = " ")
  