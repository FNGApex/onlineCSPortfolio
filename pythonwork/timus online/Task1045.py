year, amount_of_teams, sad_team = list(map(int, input().split()))
teams = dict()
for i in range(amount_of_teams):
    team = input()
    if '#' in team:
        team_name, number = team.split("#")
    if "#" not in team:
        team_name, number = team, None
    teams[team_name] = teams.get(team_name, [])
    teams[team_name].append(number)
final_team_ids = []
for i in teams.keys():
    final_team_ids.append([i, teams[i][0]])
sad_team = final_team_ids[sad_team]
print(sad_team[0], end="")
if sad_team[1] != None:
    print("#"+sad_team[1], sep="")
