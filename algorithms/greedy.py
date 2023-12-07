from solution import Sol
from collections import Counter
from input_initialization import initialize_input

# Specify your .dat file
dat_file = 'instance_n200_t12.dat'

# Initialize input
nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)


def greedy():
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
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

    # Print or use the resulting set S
    print("Resulting set S:", sol_instance.S)
    print("profit ",sol_instance.profit)
    print("used cap: ",sol_instance.used_capacities)


def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    greedy()


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
