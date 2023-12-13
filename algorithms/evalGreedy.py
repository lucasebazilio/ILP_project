from solution import Sol
from collections import Counter
from input_initialization import initialize_input
import csv
import time

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




def greedy(nOrders,nSlots,p,l,c,mindi,maxdi,maxsur):
    sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
    #print(p_sorted)
    for i in sorted_indices:
        j = mindi[i] - l[i]
        k = l[i]
        while j + k <= maxdi[i] and k > 0:
            #if(j == nSlots): print(j + k - 1, " <= ", maxdi[i])
            if sol_instance.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]

        if k == 0:
            sol_instance.insertion((i, j))

    # Print or use the resulting set S
    #print("Resulting set S:", sol_instance.S)
    #print("profit ",sol_instance.profit)
    #print("used cap: ",sol_instance.used_capacities)

    return sol_instance.profit


def main():
    with open('comparative_Greedy.csv', 'w', newline='') as csvfile:
        fieldnames = ['nOrders', 'Profit', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(100, 5200, 100):
            dat_file = f'instancesPython/instance_n{i}_t12_py.dat'
            nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_dat(dat_file)

            start_time = time.time()
            profit = greedy(nSlots=nSlots, nOrders=nOrders, p=p, l=l, c=c, mindi=mindi, maxdi=maxdi, maxsur=maxsur)
            execution_time = time.time() - start_time

            # Write results to CSV
            writer.writerow({'nOrders': nOrders, 'Profit': profit, 'Time': execution_time})



# Call the main function if the script is executed
if __name__ == "__main__":
    main()
