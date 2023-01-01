from rules import *


def points_per_card(card_name: str, troef_suit):
    points_name = 'points_value_' + str(troef_suit)
    return hierarchy_value_rules[card_name][points_name]


def suits():
    suit_choice = False
    result = ""
    while not suit_choice:
        suit = input('    Whats the troef-suit (C)lubs, (S)pades, (H)earts, (D)iamonds? ')
        try:
            result = div_suits[str(suit).lower()]
            suit_choice = True
        except Exception as e:
            print(f'Not the right input suit {e}!')
    return result


def main_players(player_north, player_east, player_south, player_west, Hand_number):
    Hand_number += 6
    if Hand_number % 4 == 0:
        return player_west
    if (Hand_number - 1) % 4 == 0:
        return player_south
    if (Hand_number - 2) % 4 == 0:
        return player_east
    if (Hand_number - 3) % 4 == 0:
        return player_north
    return 'WRONG OUTPUT main player'