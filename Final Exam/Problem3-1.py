'''''''''
Problem 3-1
You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you
 draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color?
Answer the question in reduced fraction form - eg 1/5 instead of 2/10.

Answer is 1/7
'''''''''

import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws. 
    '''
    counter = 0
    for i in range(numTrials):
        bucket = [1, 1, 1, 1, 0, 0, 0, 0]
        three_balls = random.sample(bucket, 3)
        if sum(three_balls) in [0,3]:
            counter += 1
    return counter/numTrials

print(drawing_without_replacement_sim(100000))



