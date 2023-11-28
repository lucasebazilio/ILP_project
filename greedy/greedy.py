nOrders = 4
nSlots = 12
p = [18.0, 21.0, 38.0, 6.0]
l = [2, 3, 7, 2]
c = [30.0, 15.0, 120.0, 40.0]
mindi = [2, 5, 7, 3]
maxdi = [4, 7, 8, 4]
maxsur = 30


class Sol:
    def __init__(self):
        self.S = set()
        self.used_capacities = [0] * nSlots
        self.profit = 0.0

    def insertion(self,element):
    # Element is a tuple {i,f} where we insert order i with finishing time j
        self.S.add(element)
        i,f = element
        for k in range(f - l[i]+1,f+1):
            self.used_capacities[k] += c[i]
        self.profit += p[i]

    def deletion(self,element):
    # element is a tuple {i,f} where we insert order i with finishing time j
        if self.exists(element):
            self.S.remove(element)
            i,f = element
            for k in range(f-l[i]+1,f+1):
                self.used_capacities[k] -= c[i]
            self.profit -= p[i]

    def exists(self,element):
        if element in self.S: return True
        else: return False


def greedy():
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True) # We sort P , p1 >= p2 >= ... >= pn
    #print(p_sorted)
    s = Sol()

    for i in sorted_indices:
        j = mindi[i] - l[i] + 1
        k = l[i]

        while j + k - 1 <= maxdi[i] and k > 0:
            if s.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]

        if k == 0:
            s.insertion((i, j))

    # Print or use the resulting set S
    print("Resulting set S:", s.S)
    print("profit ",s.profit)
    print("used cap: ",s.used_capacities)


def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    greedy()


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
