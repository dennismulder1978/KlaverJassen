"""
Analysing Klaverjassen cardgame to improve CPU-player
"""

print('AI klaverjas cardgame analysis')

# rules key = card name; value is list: [0] Hierarchy (int), [1] point values (int).
rules_roem = {'Jack': [1, 20],
              'Nel': [2, 14],
              'Ace': [3, 11],
              '10': [4, 10],
              'King': [5, 4],
              'Queen': [6, 3],
              '8': [7, 0],
              '7': [8, 0]}

rules_non_roem = {'Ace': [1, 11],
                  '10': [2, 10],
                  'King': [3, 4],
                  'Queen': [4, 3],
                  'Jack': [5, 2],
                  '9': [6, 0],
                  '8': [7, 0],
                  '7': [8, 0]}
