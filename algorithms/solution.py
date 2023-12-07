# solution.py
from collections import Counter

class Sol:
    def __init__(self, nOrders, nSlots, p, l, c, mindi, maxdi, maxsur):
        self.S = set()
        self.used_capacities = [0] * nSlots
        self.profit = 0.0
        self.nOrders = nOrders
        self.nSlots = nSlots
        self.p = p
        self.l = l
        self.c = c
        self.mindi = mindi
        self.maxdi = maxdi
        self.maxsur = maxsur

    def insertion(self, element):
        # Element is a tuple {i,f} where we insert order i with finishing time j
        self.S.add(element)
        i, f = element
        for k in range(f - self.l[i], f):
            self.used_capacities[k] += self.c[i]
        self.profit += self.p[i]

    def deletion(self, element):
        # element is a tuple {i,f} where we insert order i with finishing time j
        if self.exists(element):
            self.S.remove(element)
            i, f = element
            for k in range(f - self.l[i], f):
                self.used_capacities[k] -= self.c[i]
            self.profit -= self.p[i]

        return self

    def exists(self, element):
        if element in self.S:
            return True
        else:
            return False

    def isFeasible(self, i):
        j = self.mindi[i] - self.l[i]
        k = self.l[i]

        while j + k <= self.maxdi[i] and k > 0:
            if self.used_capacities[j] + self.c[i] <= self.maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = self.l[i]
        if k == 0:
            return (i, j)
        else:
            return (-1, -1)

    def evalSol(self, i):
        j = self.mindi[i] - self.l[i]
        k = self.l[i]

        while j + k <= self.maxdi[i] and k > 0:
            if self.used_capacities[j] + self.c[i] <= self.maxsur:
                j += 1
                k -= 1
            else:
                j += 1
                k = self.l[i]

        if k == 0:
            self.insertion((i, j))

    def copy(self):
        copied_sol = Sol(self.nOrders, self.nSlots, self.p, self.l, self.c, self.mindi, self.maxdi, self.maxsur)
        copied_sol.S = set(self.S)  # Copy the set
        copied_sol.used_capacities = list(self.used_capacities)  # Copy the list
        copied_sol.profit = self.profit  # Copy the float

        return copied_sol

    def compute_R_indices(self):
        R = [i for i in range(0, self.nOrders)]
        for (i, f) in self.S:
            R.remove(i)
        return R
