import random

teams = ['Reds','Blues','Greens','Yellows']
players = ['james','charlie','samantha','duke','bobby','jake']

team1 = random.choice(teams)
teams.remove(team1)
team2 = random.choice(teams)
teams.remove(team2)

team_comp1 = []
team_comp2 = []

for player in players:
	team = random.randint(1,2)
	if team == 1:
		team_comp1.append(player)
	elif team == 2:
		team_comp2.append(player)



print(team1 , team_comp1)
print(team2, team_comp2)
