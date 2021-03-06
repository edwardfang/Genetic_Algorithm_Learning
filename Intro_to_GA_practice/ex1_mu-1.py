# pylint: disable=no-member
import numpy as np
import functools

def evaluate(individual):
    return np.sum(individual)


def bitflip_mutation(bit, probability):
    if np.random.rand() < probability:
        if bit == 1:
            return 0.
        else:
            return 1.
    else:
        return bit

def geAlgorithm():
    def uniform_crossover(i1,i2):
        u = np.empty((D,))
        for i in range(D):
            # print(P[i1][i],P[i2][i])
            u[i] = np.random.choice(np.array([P[i1][i],P[i2][i]]))
        return u 
    n = 0
    t = 1
    D = 50
    mu = 20
    pm = 1/D # mutation rate

    # Algorithm 2: The initialization procedure of the population
    P = list()
    result = list()
    for i in range(mu):
        P.append(np.random.choice(np.array([0,1]),(D,)))

    terminate = False

    x_bsf = None
    value_bsf = 0

    for v in P:
        value = evaluate(v)
        result.append(evaluate(v))
        if(value>value_bsf):
            value_bsf = value
            x_bsf = v
        



    while(not terminate):
        # Step1: Mating selection: generate two distinct random number
        r = np.arange(mu)
        np.random.shuffle(r)
        selected = r[:2]
        # Step2: Variation operator : Crossover
        u = uniform_crossover(selected[0],selected[1])
        # print(u)
        # Step3: Variation operator2: Mutation
        vfunc = np.vectorize(functools.partial(bitflip_mutation, probability=pm))
        u = vfunc(u)
        # print(u)
        # Step4: Evaluate
        newvalue = evaluate(u)
        # print("New value:" + str(newvalue))
        n += 1
        # Step5: Update bsf solution
        new_value = evaluate(u)
        if(new_value >value_bsf):
            value_bsf = value
            x_bsf = u
        # Step6: Environment Selection
        selected = np.random.randint(0,mu)
        if(result[selected]<new_value):
            P[selected] = u
            result[selected] = new_value
        t +=1
        if(new_value == D):
            terminate = True

    print("# of generation:", t)
    return (t,n)

def getAverage(list, denominator, index):
    return sum([x[index] for x in count])/float(totaltimes)

if __name__ == "__main__":
    count = list()
    totaltimes = 20
    for i in range(totaltimes):
        count.append(geAlgorithm())

    print("Average # of generations %f, average evaluations %f" % (getAverage(count,totaltimes,0),getAverage(count,totaltimes,1)))

## Result average: 626.55