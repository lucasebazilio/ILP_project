import random
from collections import Counter
from solution import Sol
from input_initialization import initialize_input

# Specify your .dat file
dat_file = 'instancesPython\instance_n100_t12_py.dat'

# Initialize input
nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
# Create an instance of Sol with parameters
sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)



import random

def greedy():
    #print(p_sorted)
    for i in sorted_indices:
        j = mindi[i] - l[i]
        k = l[i]
        while j + k <= maxdi[i] and k > 0:
            if(j == nSlots): print(j + k - 1, " <= ", maxdi[i])
            if sol_instance.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]

        if k == 0:
            sol_instance.insertion((i, j))
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
    return solution

def grasp(iterations,alpha):

    best = greedy()
    best = local_search(best)
    for count in range(iterations):
        s = Sol(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)
        i = 0
        R = set(range(nOrders)) # set of indices of remaining profits to consider
        while i<nOrders:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while j < nOrders and p[sorted_indices[j]] >= p_cota:
                k,f = s.isFeasible(j)
                #print("is FEASIBLE K,F",(k,f))
                #print("j:",j)
                if k != -1:
                    RCL.add((j,f))
                    j = j + 1
                else:
                    R.remove(j)
                if not R: break
                while not (j in R) and j < nOrders: j = j + 1
            if RCL:
                m = random.choice(tuple(RCL)) # choose an element randomly from RCL
                s.insertion(m)
                R.remove(m[0])
            while not (i in R) and i < nOrders:
                i = i + 1

        s = local_search(s)

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
    grasp(iterations=20,alpha=0.2)


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
