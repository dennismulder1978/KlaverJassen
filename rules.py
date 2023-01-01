suits = {'clubs': 'Clubs',
         'spades': 'Spades',
         'hearts': 'Hearts',
         'diamonds': 'Diamonds'}

roem = {0: 'non_roem', 1: 'roem'}

rules_roem = {'Ace': {'hierarchy_roem': 3, 'points_value_roem': 11,
                      'hierarchy_non_roem': 1, 'points_value_non_roem': 11},
              '10': {'hierarchy_roem': 4, 'points_value_roem': 10,
                     'hierarchy_non_roem': 2, 'points_value_non_roem': 10},
              'King': {'hierarchy_roem': 5, 'points_value_roem': 4,
                       'hierarchy_non_roem': 3, 'points_value_non_roem': 4},
              'Queen': {'hierarchy_roem': 6, 'points_value_roem': 3,
                        'hierarchy_non_roem': 4, 'points_value_non_roem': 3},
              'Jack': {'hierarchy_roem': 1, 'points_value_roem': 20,
                       'hierarchy_non_roem': 5, 'points_value_non_roem': 2},
              '9': {'hierarchy_roem': 2, 'points_value_roem': 14,
                    'hierarchy_non_roem': 6, 'points_value_non_roem': 0},
              '8': {'hierarchy_roem': 7, 'points_value_roem': 0,
                    'hierarchy_non_roem': 7, 'points_value_non_roem': 0},
              '7': {'hierarchy_roem': 8, 'points_value_roem': 0,
                    'hierarchy_non_roem': 8, 'points_value_non_roem': 0}
              }



