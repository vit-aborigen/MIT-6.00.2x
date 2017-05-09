import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for _ in range(CURRENTRABBITPOP):
        rabbit_birth_prob = 1 - CURRENTRABBITPOP/float(MAXRABBITPOP) if CURRENTRABBITPOP < MAXRABBITPOP else 0
        if random.random() < rabbit_birth_prob:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for _ in range(CURRENTFOXPOP):
        is_fox_successed = (random.random() < (CURRENTRABBITPOP/float(MAXRABBITPOP))) and CURRENTRABBITPOP > 10
        if is_fox_successed:
            CURRENTRABBITPOP -= 1
            if random.random() < 1/float(3):
                CURRENTFOXPOP += 1
        elif CURRENTFOXPOP > 10:
            if random.random() < 0.1:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    population_rabbits = []
    population_foxes = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        population_rabbits.append(CURRENTRABBITPOP)
        population_foxes.append(CURRENTFOXPOP)
    return (population_rabbits, population_foxes)



def drawGraph(numSteps):
    population_rabbits, population_foxes = runSimulation(numSteps)
    pylab.plot(population_rabbits, label= 'Rabbits population')
    pylab.plot(population_foxes, label='Foxes population')
    pylab.title("Hunt simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Population")
    pylab.legend()
    pylab.show()

    coeff_rabbits = pylab.polyfit(range(len(population_rabbits)), population_rabbits, 2)
    pylab.plot(pylab.polyval(coeff_rabbits, range(len(population_rabbits))), label='rabbits polyfit')

    coeff_foxes = pylab.polyfit(range(len(population_foxes)), population_foxes, 2)
    pylab.plot(pylab.polyval(coeff_foxes, range(len(population_foxes))), label='foxes polyfit')
    pylab.legend()
    pylab.show()




drawGraph(200)
