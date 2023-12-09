import random
from collections import Counter
from solution import Sol
from input_initialization import initialize_input
from collections import defaultdict
import csv

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
        #print("GRASP", count,": Resulting set S:", best.S)
        #print("GRASP", count,": Profit", best.profit)
        #print("GRASP", count,": Used capacities", best.used_capacities)


    # Print or use the resulting set S from the best solution
    #print("FINAL GRASP: Resulting set S:", best.S)
    #print("FINAL GRASP: Profit", best.profit)
    #print("FINAL GRASP: Used capacities", best.used_capacities)

    return best.profit



def main():
    # Code for the main function
    average_profits = defaultdict(float) # Dictionary to store cumulative profits for each alpha
    for a in range(5, 100, 5):
        alpha_choice = a / 100  # alpha = 0.05,0.1,0.15...0.95
        print("Currently computing alpha = ",alpha_choice)
        total_profit_for_alpha = 0.0  # Accumulator for total profit for the current alpha
        for i in range(0, 50):
            dat_file = f'instances_15000_Python/instance_n15000_t12_i{i}_py.dat'
            nOrders, nSlots,p,l,c,mindi,maxdi,maxsur = initialize_dat(dat_file)
            profit = grasp(iterations=20,alpha=alpha_choice,nSlots=nSlots,nOrders=nOrders,p=p,l=l,c=c,mindi=mindi,maxdi=maxdi,maxsur=maxsur)
            total_profit_for_alpha += profit

        average_profit_for_alpha = total_profit_for_alpha / 50

        # Store the average profit in the dictionary
        average_profits[alpha_choice] = average_profit_for_alpha

    #print("Results of Alpha-Profit Dictionary")
    #print(average_profits)

    # Write the dictionary to a CSV file
    csv_file_path = 'average_profits_n15000.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Alpha', 'Average Profit'])
        for alpha, average_profit in average_profits.items():
            writer.writerow([alpha, average_profit])

    print(f"Results written to {csv_file_path}")




# Call the main function if the script is executed
if __name__ == "__main__":
    main()
