div_suits = {'clubs': 'Clubs',
             'spades': 'Spades',
             'hearts': 'Hearts',
             'diamonds': 'Diamonds',
             'c': 'Clubs',
             's': 'Spades',
             'h': 'Hearts',
             'd': 'Diamonds'
             }

troef = {0: 'non_troef',
         1: 'troef',
         'nee': 'non_troef',
         'ja': 'troef',
         'Nee': 'non_troef',
         'Ja': 'troef'
         }

hierarchy_value_rules = {'Ace': {'hierarchy_troef': 3, 'points_value_troef': 11,
                                 'hierarchy_non_troef': 1, 'points_value_non_troef': 11},
                         '10': {'hierarchy_troef': 4, 'points_value_troef': 10,
                                'hierarchy_non_troef': 2, 'points_value_non_troef': 10},
                         'King': {'hierarchy_troef': 5, 'points_value_troef': 4,
                                  'hierarchy_non_troef': 3, 'points_value_non_troef': 4},
                         'Queen': {'hierarchy_troef': 6, 'points_value_troef': 3,
                                   'hierarchy_non_troef': 4, 'points_value_non_troef': 3},
                         'Jack': {'hierarchy_troef': 1, 'points_value_troef': 20,
                                  'hierarchy_non_troef': 5, 'points_value_non_troef': 2},
                         '9': {'hierarchy_troef': 2, 'points_value_troef': 14,
                               'hierarchy_non_troef': 6, 'points_value_non_troef': 0},
                         '8': {'hierarchy_troef': 7, 'points_value_troef': 0,
                               'hierarchy_non_troef': 7, 'points_value_non_troef': 0},
                         '7': {'hierarchy_troef': 8, 'points_value_troef': 0,
                               'hierarchy_non_troef': 8, 'points_value_non_troef': 0}
                         }



