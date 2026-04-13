class Player():
    def __init__(self, name, goals, team, position):
        self.name = name
        self.goals = goals
        self.team = team
        self.position = position

    def biography(self):
        print(f'The player {self.name} plays in the team {self.team} on the position {self.position} and has scored {self.goals} goals.')

    def plus_goal(self):
        self.goals += 1
        print(f'YEEAAAAAAH!!! {self.name} has scored a goal!')

maksim = Player('Maksim', 3, 'GroBro', 'Defender')
trond = Player('Trond', 12, 'GroBro', 'Attacker')
trond.biography()
maksim.biography()
maksim.plus_goal()
print(maksim.goals)


