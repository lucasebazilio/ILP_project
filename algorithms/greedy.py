from solution import Sol
from collections import Counter
import configparser
from configparser import ConfigParser, ExtendedInterpolation
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
