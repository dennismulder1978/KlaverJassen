from rules import *


def points_per_card(card_name: str, roem_sign):
    points_name = 'points_value_' + str(roem_sign)
    return rules_roem[card_name][points_name]