info = input().split(' ')
team_a_players = 11
team_b_players = 11
players_loses = []
condition = False

for card in info:
    if card not in players_loses:
        players_loses.append(card)
        if 'A' in card:
            team_a_players -= 1
        if 'B' in card:
            team_a_players -= 1

        if team_a_players < 7 or team_b_players < 7:
            condition = True
            break

print(f'Team A - {team_a_players}; Team B - {team_b_players}')

if condition:
    print('Game was terminated')





# MIN_PLAYERS = 7
# team_a = list(range(1, 12))
# team_b = list(range(1, 12))
# terminated = False
#
#
# cards_list = input().split()
#
# for card in cards_list:
#
#     team, player_num = card.split('-')
#     player_num = int(player_num)
#
#     if 'A' in team:
#         if player_num in team_a:
#             team_a.remove(player_num)
#
#     elif 'B' in team:
#         if player_num in team_b:
#             team_b.remove(player_num)
#
#     if len(team_a) < MIN_PLAYERS or len(team_b) < MIN_PLAYERS:
#         terminated = True
#         break
#
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
#
# if terminated:
#     print('Game was terminated')







# card = 0

# while game_on:

#     if cards_list[card][0].lower() == 'a':
#         try:
#             team_a.pop(int(cards_list[card][-1]))
#         except:
#             pass

#     elif cards_list[card][0].lower() == 'b':
#         try:
#             team_b.pop(int(cards_list[card][-1]))
#         except:
#             pass

#     if len(team_a) < 7 or len(team_b) < 7:
#         game_on = False
#         break

#     if card == len(cards_list) - 1:
#         break

#     card += 1


# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

# if not game_on:
#     print('Game was terminated')
