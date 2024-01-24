import pandas as pd
import csv, sys

pd.options.display.float_format = '{:.0f}'.format

all_teams = pd.read_csv('teams.csv')

# n = 0
# while n < 30:
#   print(all_teams.iloc[n])
#   n += 1

# print(all_teams.iloc[20])

# keep_going = True

# while keep_going:

#   team_search = input('Which team do you want to search for? (ex. SAS) >> ').upper()
#   searched_team = all_teams[all_teams.ABBREVIATION.eq(team_search)]

#   print(team_search)
#   print(searched_team)

#   keep_going_yn = input('Search again? (Y/N) >> ' ).upper()

#   if keep_going_yn == 'N':
#     keep_going = False

# one_team = all_teams.loc[lambda x: x['ABBREVIATION'] == 'SAS']
# print(one_team)

# teams = ['SAS', 'LAL', 'GSW', 'MIA']
# print(all_teams[all_teams.ABBREVIATION.isin(teams)])

# x = open('ranking.csv')
# filename = 'players.csv'

# with open(filename, newline = '') as f:
#   reader = csv.reader(f)

#   try:
#     for row in reader:
#       print(row)
#   except csv.Error as e:
#     sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
#   else:
#     print('less whack shit dawg')
#   finally:
#     x.close()

# print(x.closed)

all_games = pd.read_csv('games.csv')
game_date = input('Enter a game date you want to see all the games of? (Ex. 2012-05-10) >> ')

games_on_date = all_games.loc[lambda x: x['GAME_DATE_EST'] == game_date]
searched_game_info = games_on_date.loc[:, ['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'PTS_home', 'PTS_away', 'HOME_TEAM_WINS']]
print(games_on_date)
print(searched_game_info)

def find_team(team_id):
  team_info = all_teams.loc[lambda x: x['TEAM_ID'] == team_id]
  team_city = team_info['CITY'].values[0]
  team_nickname = team_info['NICKNAME'].values[0]
  team_name = team_city + ' ' + team_nickname
  
  return team_name

n = 0
while n < len(searched_game_info):
  temp_game = searched_game_info.iloc[n]
  home_team_id = temp_game.loc['HOME_TEAM_ID']
  home_score = int(temp_game.loc['PTS_home'])
  visitor_team_id = temp_game.loc['VISITOR_TEAM_ID']
  away_score = int(temp_game.loc['PTS_away'])

  if temp_game.loc['HOME_TEAM_WINS']:
    print(f'On {game_date}, the home team {find_team(home_team_id)} beat the {find_team(visitor_team_id)} by a score of {home_score} to {away_score}')
  else:
    print(f'On {game_date}, the home team {find_team(home_team_id)} lost to the {find_team(visitor_team_id)} by a score of {home_score} to {away_score}')

  n+=1