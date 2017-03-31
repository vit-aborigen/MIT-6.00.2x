import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    random.randrange(10,22, 2)

print(deterministicNumber())
