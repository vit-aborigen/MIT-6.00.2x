import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    counter = 0
    for i in range(numTrials):
        bucket = [1, 1, 1, 0, 0, 0]
        for idx in range(3):
            bucket.pop(random.randint(0, len(bucket)-1))
        if sum(bucket) in [0,3]:
            counter += 1
    return counter/numTrials

print(noReplacementSimulation(2000))

