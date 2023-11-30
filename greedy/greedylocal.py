import random
from collections import Counter

nOrders = 4
nSlots = 12
p = [75.0, 75.0, 100.0, 100.0]
l = [2, 3, 7, 12]
c = [30.0, 15.0, 120.0, 30.0]
mindi = [2, 5, 7, 7]
maxdi = [4, 7, 8, 12]
maxsur = 30
sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True) # We sort P , p1 >= p2 >= ... >= pn


class Sol:
    def __init__(self):
        self.S = set()
        self.used_capacities = [0] * nSlots
        self.profit = 0.0

    def insertion(self, element):
        # Element is a tuple {i,f} where we insert order i with finishing time j
        self.S.add(element)
        i, f = element
        for k in range(f - l[i] + 1, f + 1):
            self.used_capacities[k] += c[i]
        self.profit += p[i]

    def deletion(self, element):
        # element is a tuple {i,f} where we insert order i with finishing time j
        if self.exists(element):
            self.S.remove(element)
            i, f = element
            for k in range(f - l[i] + 1, f + 1):
                self.used_capacities[k] -= c[i]
            self.profit -= p[i]

        return self

    def exists(self, element):
        if element in self.S:
            return True
        else:
            return False

    def evalSol(self, i):
        j = mindi[i] - l[i] + 1
        k = l[i]

        while j + k - 1 <= maxdi[i] and k > 0:
            if self.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]
        if k == 0:
            self.insertion((i, j))


    def isFeasible(self, i):
        j = mindi[i] - l[i] + 1
        k = l[i]

        while j + k - 1 <= maxdi[i] and k > 0:
            if self.used_capacities[j] + c[i] <= maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = l[i]
        if k == 0:
            return (i,j)
        else: return (-1,-1)

    def copy(self):
        copied_sol = Sol()
        copied_sol.S = set(self.S)  # Copy the set
        copied_sol.used_capacities = list(self.used_capacities)  # Copy the list
        copied_sol.profit = self.profit  # Copy the float

        return copied_sol

    def compute_R_indices(self):
        R = [i for i in range(0, nOrders)]
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
    print("GL:profit ", s.profit)
    print("GL:used cap: ", s.used_capacities)


import random

def greedy():

    #print(p_sorted)
    s = Sol()

    for i in sorted_indices:
        s.evalSol(i)
    return s

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

def grasp(iterations,alpha):


    best = greedy()
    local_search(best)
    count = 0
    while (count != iterations):
        count = count + 1
        s = Sol()
        i = 0
        P_remaining = set(range(nOrders)) # set of indices of remaining profits to consider
        while P_remaining:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while P_remaining and p[sorted_indices[j]] >= p_cota:
                k,f = s.isFeasible(j)
                #print("is FEASIBLE K,F",(k,f))
                #print("j:",j)
                if k != -1:
                    RCL.add((j,f))
                    j = j + 1
                else:
                    if j in P_remaining: P_remaining.remove(j)
                while P_remaining and not (j in P_remaining): j = j + 1
            if RCL:
                m = random.choice(tuple(RCL)) # choose an element randomly from RCL
                s.insertion(m)
                P_remaining.remove(m[0])
            while P_remaining and not (i in P_remaining):
                i = i + 1

        local_search(s)

        if s.profit > best.profit:
            best = s.copy()

    print("S.profit = ", s.profit)
    # Print or use the resulting set S from the best solution
    print("GRASP: Resulting set S:", best.S)
    print("GRASP: Profit", best.profit)
    print("GRASP: Used capacities", best.used_capacities)



def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    grasp(iterations=1,alpha=0.75)


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
