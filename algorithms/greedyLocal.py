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
    print("GL:Resulting set S:", sol_instance.S)
    print("GL:profit ", sol_instance.profit)
    print("GL:used cap: ", sol_instance.used_capacities)


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
