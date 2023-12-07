import random
from collections import Counter
import configparser
from configparser import ConfigParser, ExtendedInterpolation
from solution import Sol

config = configparser.ConfigParser()
config.read('sampleInstance.dat')

# Access values using the section and option
nOrders = config.getint('Values', 'nOrders')
nSlots = config.getint('Values', 'nSlots')
p = config.get('Values', 'p')
l = config.get('Values', 'l')
c = config.get('Values', 'c')
mindi = config.get('Values', 'mindi')
maxdi = config.get('Values', 'maxdi')
maxsur = config.getfloat('Values', 'maxsur')

# Parse string lists into actual lists
p = [float(val) for val in p.strip('[]').split(',')]
l = [int(val) for val in l.strip('[]').split(',')]
c = [float(val) for val in c.strip('[]').split(',')]
mindi = [int(val) for val in mindi.strip('[]').split(',')]
maxdi = [int(val) for val in maxdi.strip('[]').split(',')]

sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
# Create an instance of Sol with parameters
sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)



def greedy_local():
    s_old = greedy()
    r_indices = s_old.compute_R_indices()
    p_old = s_old.profit

    for (i, f) in s_old.S:
        s = s_old.copy()
        s.deletion((i, f))
        for j in r_indices:
            s.evalSol(j)
        if (p_old < s.profit):
            s_old = s.copy()
            p_old = s.profit

    # Print or use the resulting set S
    print("GL:Resulting set S:", s.S)
    print("GL:profit ", s.profit)
    print("GL:used cap: ", s.used_capacities)


import random

def greedy():

    #print(p_sorted)
    for i in sorted_indices:
        sol_instance.evalSol(i)
    return sol_instance

def local_search(solution):
    r_indices = solution.compute_R_indices()
    p_old = solution.profit

    for (i, f) in solution.S:
        s = solution.copy()
        s.deletion((i, f))
        for j in r_indices:
            s.evalSol(j)
        if p_old < s.profit:
            solution = s.copy()
            p_old = s.profit

def grasp(iterations,alpha):

    best = greedy()
    local_search(best)
    for count in range(iterations):
        i = 0
        P_remaining = set(range(nOrders)) # set of indices of remaining profits to consider
        while P_remaining and i<nOrders:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while P_remaining and j < nOrders and p[sorted_indices[j]] >= p_cota:
                k,f = sol_instance.isFeasible(j)
                #print("is FEASIBLE K,F",(k,f))
                #print("j:",j)
                if k != -1:
                    RCL.add((j,f))
                    j = j + 1
                else:
                    if j in P_remaining: P_remaining.remove(j)
                while P_remaining and not (j in P_remaining) and j < nOrders: j = j + 1
            if RCL:
                m = random.choice(tuple(RCL)) # choose an element randomly from RCL
                sol_instance.insertion(m)
                P_remaining.remove(m[0])
            while P_remaining and not (i in P_remaining) and i < nOrders:
                i = i + 1

        local_search(sol_instance)

        if sol_instance.profit > best.profit:
            best = sol_instance.copy()

        # Print or use the resulting set S from the best solution
        print("GRASP", count,": Resulting set S:", best.S)
        print("GRASP", count,": Profit", best.profit)
        print("GRASP", count,": Used capacities", best.used_capacities)


    # Print or use the resulting set S from the best solution
    print("FINAL GRASP: Resulting set S:", best.S)
    print("FINAL GRASP: Profit", best.profit)
    print("FINAL GRASP: Used capacities", best.used_capacities)



def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    grasp(iterations=20,alpha=0.75)


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
