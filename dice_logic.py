import random

def getRolls(numRolls, diceSize):
    rolls = []
    for i in range(numRolls):
        rolls.append(random.randint(1,diceSize))
    return rolls

def getRollSum(rolls, size):
    if size == 0:
        return 0
    else:
        return rolls[size - 1] + getRollSum(rolls, size - 1)