import random
from collections import Counter
from solution import Sol
from input_initialization import initialize_input

# Specify your .dat file
dat_file = 'instancesPython/instance_n15000_t12_py.dat'

# Initialize input
nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
# Create an instance of Sol with parameters
sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)



import random

def greedy():

    #print(p_sorted)
    s = Sol(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)

    for i in sorted_indices:
        s.evalSol(i)
    return s

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
        s = Sol(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)
        i = 0
        P_remaining = set(range(nOrders)) # set of indices of remaining profits to consider
        while P_remaining and i<nOrders:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while P_remaining and j < nOrders and p[sorted_indices[j]] >= p_cota:
                k,f = s.isFeasible(j)
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
                s.insertion(m)
                P_remaining.remove(m[0])
            while P_remaining and not (i in P_remaining) and i < nOrders:
                i = i + 1

        local_search(s)

        if s.profit > best.profit:
            best = s.copy()

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
    grasp(iterations=100,alpha=0.3)


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
