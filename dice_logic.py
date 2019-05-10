import random

"""
	returns a list of random numbers between 1 and diceSize, of length numRolls 
"""
def getRolls(numRolls, diceSize):
    rolls = []
    for i in range(numRolls):
        rolls.append(random.randint(1, diceSize))
    return rolls

"""
	takes a list of integers (rolls) and the list size and returns the sum of all elements
"""
def getRollSum(rolls, size):
    if size == 0:
        return 0
    else:
        return rolls[size - 1] + getRollSum(rolls, size - 1)