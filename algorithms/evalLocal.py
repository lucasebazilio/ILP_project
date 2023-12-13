from collections import Counter
from input_initialization import initialize_input
from solution import Sol
import time
import csv

# Specify your .dat file
#dat_file = 'instancesPython/instance_n100000_t12_py.dat'

# Initialize input
#nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

#sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)

def initialize_dat(dat_file):
    # Initialize input
    nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
    # Create an instance of Sol with parameters
    sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)

    return nOrders,nSlots,p,l,c,mindi,maxdi,maxsur # return instance information



def greedy_local(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur):
    s_old = greedy(nSlots=nSlots, nOrders=nOrders, p=p, l=l, c=c, mindi=mindi, maxdi=maxdi, maxsur=maxsur)
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
    #print("GL:Resulting set S:", s.S)
    #print("GL:profit ", s.profit)
    #print("GL:used cap: ", s.used_capacities)

    return s.profit


def greedy(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur):
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
    sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)
    # print(p_sorted)
    for i in sorted_indices:
        sol_instance.evalSol(i)

    # Print or use the resulting set S
    #print("Resulting set S:", sol_instance.S)
    #print("profit ", sol_instance.profit)
    #print("used cap: ", sol_instance.used_capacities)

    return sol_instance


def main():
    with open('comparative_LocalSearch.csv', 'w', newline='') as csvfile:
        fieldnames = ['nOrders', 'Profit', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(100, 5200, 100):
            dat_file = f'instancesPython/instance_n{i}_t12_py.dat'
            nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_dat(dat_file)

            start_time = time.time()
            profit = greedy_local(nSlots=nSlots, nOrders=nOrders, p=p, l=l, c=c, mindi=mindi, maxdi=maxdi, maxsur=maxsur)
            execution_time = time.time() - start_time

            # Write results to CSV
            writer.writerow({'nOrders': nOrders, 'Profit': profit, 'Time': execution_time})


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
