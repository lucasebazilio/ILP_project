nOrders = 4
nSlots = 12
p = [18.0, 21.0, 38.0, 6.0]
l = [2, 3, 7, 2]
c = [30.0, 15.0, 120.0, 40.0]
mindi = [2, 3, 7, 3]
maxdi = [4, 7, 8, 4]
maxsur = 30


def greedy():
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True) # We sort P , p1 >= p2 >= ... >= pn
    #print(p_sorted)
    s = set()
    used_capacities = [0] * nSlots

    for i in sorted_indices:
        j = mindi[i] - l[i] + 1
        k = l[i]

        while j + k - 1 <= maxdi[i] and k > 0:
            if used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]

        if k == 0:
            s.add((i, j, c[i]))

    # Print or use the resulting set S
    print("Resulting set S:", s)


def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    greedy()


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
