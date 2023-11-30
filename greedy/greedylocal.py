nOrders = 4
nSlots = 12
p = [75.0, 75.0, 100.0, 100.0]
l = [2, 3, 7, 12]
c = [30.0, 15.0, 120.0, 30.0]
mindi = [2, 5, 7, 7]
maxdi = [4, 7, 8, 12]
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
        for k in range(f - l[i],f):
            self.used_capacities[k] += c[i]
        self.profit += p[i]

    def deletion(self,element):
    # element is a tuple {i,f} where we insert order i with finishing time j
        if self.exists(element):
            self.S.remove(element)
            i,f = element
            for k in range(f-l[i],f):
                self.used_capacities[k] -= c[i]
            self.profit -= p[i]

        return self

    def exists(self,element):
        if element in self.S: return True
        else: return False


    def evalSol(self,i):
        j = mindi[i] - l[i]
        k = l[i]

        while j + k <= maxdi[i] and k > 0:
            if self.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]

        if k == 0:
            self.insertion((i, j))
            
    def copy(self):
        copied_sol = Sol()
        copied_sol.S = set(self.S)  # Copy the set
        copied_sol.used_capacities = list(self.used_capacities)  # Copy the list
        copied_sol.profit = self.profit  # Copy the float

        return copied_sol

    def compute_R_indices(self):
        R = [i for i in range(0,nOrders)]
        for (i, f) in self.S:
            R.remove(i)
        return R

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
    print("GL:Resulting set S:", s.S)
    print("GL:profit ",s.profit)
    print("GL:used cap: ",s.used_capacities)

def greedy():
    sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True) # We sort P , p1 >= p2 >= ... >= pn
    #print(p_sorted)
    s = Sol()

    for i in sorted_indices:
        s.evalSol(i)

    # Print or use the resulting set S
    print("Resulting set S:", s.S)
    print("profit ",s.profit)
    print("used cap: ",s.used_capacities)

    return s


def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    greedy_local()


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
