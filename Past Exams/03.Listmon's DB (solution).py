class Player:
    def __init__(self, name, games_results):
        self.name = name
        self.games_results = games_results

    def get_count_games(self):
        return len(self.games_results)

    def get_score_from_games(self):
        return  sum(self.games_results)

data = input()
players_DB = []

while not data == 'report':
    player_name = data.split(' -> ')[0]
    games_results = data.split(' -> ')[1].split(', ')

    player = Player(player_name, list(map(int, games_results)))
    players_DB.append(player)

    data = input()

report_data = input()

while not report_data == 'end':
    command = report_data.split()[0]
    ordering = report_data.split()[1]

    sorted_players = []

    if command == 'score':
        if ordering == 'ascending':
            sorted_players = sorted(players_DB, key=lambda x: (x.get_score_from_games(), x.name))
        else:
            sorted_players = sorted(players_DB, key=lambda x: (-x.get_score_from_games(), x.name))

        for player in sorted_players:
            print(f'{player.name}: {player.get_score_from_games()}')

    else:
        if ordering == 'ascending':
            sorted_players = sorted(players_DB, key=lambda x: (x.get_count_games(), x.name))
        else:
            sorted_players = sorted(players_DB, key=lambda x: (-x.get_count_games(), x.name))

        for player in sorted_players:
            print(f'{player.name}: {player.get_count_games()}')

    report_data = input()