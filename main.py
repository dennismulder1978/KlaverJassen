"""
Analysing Klaverjassen cardgame to improve CPU-player
"""

print('AI klaverjas cardgame analysis')

# rules key = card name; value is list: [0] Hierarchy (int), [1] point values (int).
rules_roem = {'Jack': {'hierarchy': 1, 'points_value': 20},
              '9': {'hierarchy': 2, 'points_value': 14},
              'Ace': {'hierarchy': 3, 'points_value': 11},
              '10': {'hierarchy': 4, 'points_value': 10},
              'King': {'hierarchy': 5, 'points_value': 4},
              'Queen': {'hierarchy': 6, 'points_value': 3},
              '8': {'hierarchy': 7, 'points_value': 0},
              '7': {'hierarchy': 8, 'points_value': 0}}

rules_non_roem = {'Ace': {'hierarchy': 1, 'points_value': 11},
                  '10': {'hierarchy': 2, 'points_value': 10},
                  'King': {'hierarchy': 3, 'points_value': 4},
                  'Queen': {'hierarchy': 4, 'points_value': 3},
                  'Jack': {'hierarchy': 5, 'points_value': 2},
                  '9': {'hierarchy': 6, 'points_value': 0},
                  '8': {'hierarchy': 7, 'points_value': 0},
                  '7': {'hierarchy': 8, 'points_value': 0}}

print('Non roem:')
for card in rules_non_roem.keys():
    print(f"{card}, {rules_non_roem[card]['points_value']}, {rules_non_roem[card]['hierarchy']}")
print('Roem:')
for card in rules_roem.keys():
    print(f"{card}, {rules_roem[card]['points_value']}, {rules_roem[card]['hierarchy']}")
