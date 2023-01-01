"""
Analysing Klaverjassen cardgame to improve CPU-player

Instruction: roem[0] = non-roem; roem[1] = roem;
Cards are: ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7'] # as strings!
"""
from functions import *
from rules import suits

roem_suit = suits[str(input('Whats the roem-suit? ')).lower()]
print(roem_suit)

print(points_per_card('Jack', roem[0]) + points_per_card('9', roem[1]))


