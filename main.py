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
# ## Basic parameters
Hand_number = 1

# ## register players/ teams north-south and east-west.
player_north = str(input("Who is the first main player (player 'north')? "))
player_east = str(input("Who is the following player (player 'east')? "))
player_south = str(input("Who is the following player (player 'south')? "))
player_west = str(input("Who is the last player (player 'west')? "))
team_North_South = player_north + ' ' + player_south
team_East_West = player_east + ' ' + player_west
# ## creating game_scoring_table
game_scoring_table = pd.DataFrame(columns=[team_North_South, team_East_West])


# ## testing
# TODO delete testing when done
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]
game_scoring_table.loc[len(game_scoring_table.index)] = [2, 3]
print(f"{player_north}, {player_east}, {player_south}, {player_west}.", end="\n\n")
print(game_scoring_table)

# start a new hand, deck is shuffled, each player receives 8 cards.

# ## Basic parameters
cards_played_record = pd.DataFrame(columns=['hand_number',
                                            'round_number',
                                            'round_player',
                                            'card_north',
                                            'card_east',
                                            'card_south',
                                            'card_west',
                                            'points-north_south',
                                            'points_east_west'])
round_number = 1

while Hand_number < 17:
    main_player = main_players(player_north, player_east, player_south, player_west, Hand_number)

    print(f"The hand number is: {Hand_number}")
    if Hand_number > 1:
        print(f"    Score team {player_north}/ {player_south}: {game_scoring_table.iloc[:, 0].sum()}.")
        print(f"    Score team {player_east}/ {player_west}: {game_scoring_table.iloc[:, 1].sum()}.")
    print(f'The main player is (deals first card):{main_player}')

    # ask for troef_suit
    troef_suit = suits()
    print(troef_suit, end='\n\n')



    Hand_number += 1
    # TODO determine main_player
    # TODO input each card
    # TODO record played cards in a pd.DataFrame
    #  ## determine per hand winner en end-points
    #  ## add final score to game_scoring_table
