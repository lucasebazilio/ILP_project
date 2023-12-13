from collections import Counter
from input_initialization import initialize_input
from solution import Sol

# Specify your .dat file
dat_file = 'instancesPython\instance_n100_t12_py.dat'

# Initialize input
nOrders, nSlots, p, l, c, mindi, maxdi, maxsur = initialize_input(dat_file)

sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)


def greedy_local():
    s_old = greedy()
    print("GREEDY:profit ", s_old.profit)
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


def greedy():
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
    # print(p_sorted)
    for i in sorted_indices:
        sol_instance.evalSol(i)

    # Print or use the resulting set S
    print("Resulting set S:", sol_instance.S)
    print("profit ", sol_instance.profit)
    print("used cap: ", sol_instance.used_capacities)

    return sol_instance


def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    greedy_local()


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
