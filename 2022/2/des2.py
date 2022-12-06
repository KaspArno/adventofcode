shape_values = {'x' : 1, 'y': 2, 'z' : 3}

def getPoints(me, outcome):
    shape_values = {'rock' : 1, 'paper': 2, 'sissors' : 3}
    outcome_values = {'loose' : 0, 'tie' : 3, 'win' : 6}

    return shape_values[me] + outcome_values[outcome]


def getShape(shape):
    shape = shape.lower()
    if (shape == 'a' or shape == 'x'): return 'rock'
    if (shape == 'b' or shape == 'y'): return 'paper'
    if (shape == 'c' or shape == 'z'): return 'sissors'

def matchResult(me, oponent):
    if (me == oponent): return 'tie'
    if ((me == 'rock' and oponent == 'sissors') or (me == 'sissors' and oponent == 'paper') or (me == 'paper' and oponent == 'rock')): return 'win'
    return 'loose'

def myShape(oponent_shape, needed_outcome):
    if (needed_outcome == 'tie'): return oponent_shape
    if (needed_outcome == 'loose'):
        if (oponent_shape == 'rock'): return 'sissors'
        if (oponent_shape == 'sissors'): return 'paper'
        if (oponent_shape == 'paper'): return 'rock'
    if (needed_outcome == 'win'):
        if (oponent_shape == 'rock'): return 'paper'
        if (oponent_shape == 'sissors'): return 'rock'
        if (oponent_shape == 'paper'): return 'sissors'

total_points = 0
outcome = {'X' : 'loose', 'Y' : 'tie', 'Z' : 'win'}

with open('2/input.txt') as input:
    for line in input.readlines():
        line = line.strip()
        oponent, needed_outcome_char = line.split()
        needed_outcome = outcome[needed_outcome_char]

        oponent_shape = getShape(oponent)
        my_shape = myShape(oponent_shape, needed_outcome)
        total_points += getPoints(my_shape, needed_outcome)
print(total_points)