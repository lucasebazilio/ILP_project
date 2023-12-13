import random
from collections import Counter
from solution import Sol
from input_initialization import initialize_input
from collections import defaultdict
import csv
import time
import numpy as np

'''
# Specify your .dat file
dat_file = 'instancesPython/instance_n15000_t12_py.dat'

# Initialize input
nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
# Create an instance of Sol with parameters
sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)
'''

def initialize_dat(dat_file):
    # Initialize input
    nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
    # Create an instance of Sol with parameters
    sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)

    return nOrders,nSlots,p,l,c,mindi,maxdi,maxsur # return instance information




def greedy(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur):
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)
    #print(p_sorted)
    s = Sol(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)

    for i in sorted_indices:
        s.evalSol(i)
    return s, sorted_indices

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

def grasp(iterations,alpha,nOrders,nSlots,p,l,c,mindi,maxdi,maxsur):

    best,sorted_indices = greedy(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)
    local_search(best)
    for _ in range(iterations):
        s = Sol(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur)
        i = 0
        R = set(range(nOrders)) # set of indices of remaining profits to consider
        while i<nOrders:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while j < nOrders and p[sorted_indices[j]] >= p_cota:
                k,f = s.isFeasible(j)
                if k != -1:
                    RCL.add((j,f))
                    j = j + 1
                else:
                    if j in R: R.remove(j)
                if not R: break
                while not (j in R) and j < nOrders: j = j + 1
            if RCL:
                m = random.choice(tuple(RCL)) # choose an element randomly from RCL
                s.insertion(m)
                R.remove(m[0])
            while not (i in R) and i < nOrders:
                i = i + 1

        local_search(s)

        if s.profit > best.profit:
            best = s.copy()
    return best.profit



def main():
    with open('comparative_Grasp.csv', 'w', newline='') as csvfile:
        fieldnames = ['nOrders', 'Profit', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(100, 5200, 100):
            dat_file = f'instancesPython/instance_n{i}_t12_py.dat'
            print("Currently in n = ",i)
            nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_dat(dat_file)

            start_time = time.time()
            profit = grasp(iterations=60,alpha=0.15,nSlots=nSlots,nOrders=nOrders,p=p,l=l,c=c,mindi=mindi,maxdi=maxdi,maxsur=maxsur)
            execution_time = time.time() - start_time

            # Write results to CSV
            writer.writerow({'nOrders': nOrders, 'Profit': profit, 'Time': execution_time})




# Call the main function if the script is executed
if __name__ == "__main__":
    main()