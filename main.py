"""
Analysing Klaverjassen cardgame to improve CPU-player

Instruction: troef[0/nee] = non-troef; troef[1/ja] = troef;
Cards are: ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7'] # as strings!
i.e.: points_per_card('Jack', troef['nee'])

a 'game' is the total rounds played whom ever first reach 2592 points (=4 players x 4 hands x 162 points per hand).
a 'hand' is playing 8 rounds/ cards after dealing (resulting in all cards played!)
a 'round' is when each of the 4 players each play 1 card

the main player (starts with north, each hand passes clockwise)
"""
from functions import *
import pandas as pd

# Start a new game

# ## register players/ teams north-south and east-west.
player_north = str(input("Who is the first main player (player 'north')? "))
player_east = str(input("Who is the following player (player 'east')? "))
player_south = str(input("Who is the following player (player 'south')? "))
player_west = str(input("Who is the last player (player 'west')? "))
player_list = [player_north, player_east, player_south, player_west]
basic_player_list = ['player_north', 'player_east', 'player_south', 'player_west']


# ## creating game_scoring_table
team_North_South = player_north + ' - ' + player_south
team_East_West = player_east + ' - ' + player_west
game_scoring_table = pd.DataFrame(columns=[team_North_South, team_East_West])

# ## testing
# TODO delete testing when done
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]

# start a new hand, deck is shuffled, each player receives 8 cards.
# ## Basic parameters
cards_played_record = pd.DataFrame(columns=['hand_number',
                                            'round_number',
                                            'round_player',
                                            'troef_suit',
                                            'card_player_north',
                                            'card_player_east',
                                            'card_player_south',
                                            'card_player_west',
                                            'card_points_north_south',
                                            'card_points_east_west',
                                            'roem_points_north_south',
                                            'roem_points_east_west'])
# ## Start of the game
hand_number = 1
round_number = 1

# TODO SETUP: please delete after completion
punten_nz = 5
punten_ew = 6
roem_nz = 7
roem_ew = 8

while hand_number < 17:
    main_player = player_list[hand_number % 4 - 1]
    dealer = player_list[hand_number % 4 - 2]
    print(f"The hand number is: {hand_number}, round: {round_number}")
    if hand_number > 1:
        print(f"    Score team {team_North_South}: {game_scoring_table.iloc[:, 0].sum()}.")
        print(f"    Score team {team_East_West}: {game_scoring_table.iloc[:, 1].sum()}.")
    print(f'    The dealer is {dealer}, the main player is {main_player}.')

    # ask for troef_suit
    troef_suit = suits()

    # record 4 cards per round:
    basic_card_played_list = ['card_player_a', 'card_player_b', 'card_player_c', 'card_player_d']
    card_player_a = input(f'What did {player_list[hand_number % 4 - 1]} give? ')
    card_player_b = input(f'What did {player_list[hand_number % 4]} give? ')
    card_player_c = input(f'What did {player_list[hand_number % 4 - 3]} give? ')
    card_player_d = input(f'What did {player_list[hand_number % 4 - 2]} give? ')

    card_player_north = basic_card_played_list[hand_number % 4 - 1]
    card_player_east = basic_card_played_list[hand_number % 4]
    card_player_south = basic_card_played_list[hand_number % 4 - 3]
    card_player_west = basic_card_played_list[hand_number % 4 - 2]
    #
    # if card_player_a[0] == basic_player_list[0]:
    #     card_player_north = card_player_a[1]
    # elif card_player_a[0] == basic_player_list[1]:
    #     card_player_east = card_player_a[1]
    # elif card_player_a[0] == basic_player_list[2]:
    #     card_player_south = card_player_a[1]
    # elif card_player_a[0] == basic_player_list[3]:
    #     card_player_west = card_player_a[1]
    #
    # if card_player_b[0] == basic_player_list[0]:
    #     card_player_north = card_player_b[1]
    # elif card_player_b[0] == basic_player_list[1]:
    #     card_player_east = card_player_b[1]
    # elif card_player_b[0] == basic_player_list[2]:
    #     card_player_south = card_player_b[1]
    # elif card_player_b[0] == basic_player_list[3]:
    #     card_player_west = card_player_b[1]
    #
    # if card_player_c[0] == basic_player_list[0]:
    #     card_player_north = card_player_c[1]
    # elif card_player_c[0] == basic_player_list[1]:
    #     card_player_east = card_player_c[1]
    # elif card_player_c[0] == basic_player_list[2]:
    #     card_player_south = card_player_c[1]
    # elif card_player_c[0] == basic_player_list[3]:
    #     card_player_west = card_player_a[1]
    #
    # if card_player_d[0] == basic_player_list[0]:
    #     card_player_north = card_player_d[1]
    # elif card_player_d[0] == basic_player_list[1]:
    #     card_player_east = card_player_d[1]
    # elif card_player_d[0] == basic_player_list[2]:
    #     card_player_south = card_player_d[1]
    # elif card_player_d[0] == basic_player_list[3]:
    #     card_player_west = card_player_d[1]

    cards_played_record.loc[len(cards_played_record.index)] = [hand_number,
                                                               round_number,
                                                               basic_player_list[hand_number % 4 - 1],
                                                               troef_suit,
                                                               card_player_north,
                                                               card_player_east,
                                                               card_player_south,
                                                               card_player_west,
                                                               punten_nz,
                                                               punten_ew,
                                                               roem_nz,
                                                               roem_ew]
    round_number += 1

    # TEST

    # print(f'    a:{card_player_a[0]}:{card_player_a[1]},\n'
    #       f'    b:{card_player_b[0]}:{card_player_b[1]},\n'
    #       f'    c: {card_player_c[0]}:{card_player_c[1]},\n'
    #       f'    d: {card_player_d[0]}:{card_player_d[1]}.\n')

    print(cards_played_record)


hand_number += 1
    # TODO record played cards in a pd.DataFrame
    #  ## determine per hand winner en end-points
    #  ## add final score to game_scoring_table


# finally
# TODO write game_scoring_table to CSV
# printout end results.
cards_played_record.to_csv('test.csv')