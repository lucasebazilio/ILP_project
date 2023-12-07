import random
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

sorted_indices = sorted(range(len(p)), key=lambda k: p[k], reverse=True)  # We sort P , p1 >= p2 >= ... >= pn
# Create an instance of Sol with parameters
sol_instance = Sol(nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)


"""
nOrders=100
nSlots=12
p=[38.20894719528405, 198.84208295810714, 14.653236903406896, 128.06497497588393, 104.05795445291159, 32.92495389233441, 2.999739456658479, 121.29362254717064, 56.44007934588458, 186.80323203392464, 178.89127946672247, 30.41257963965245, 176.5947427329842, 63.914332302943166, 166.4220775985847, 180.44697857798266, 91.26895937114008, 100.20215193823552, 161.8460604060256, 147.43303461206744, 139.88213964583989, 15.266641450182128, 2.130067069001629, 13.795270597582387, 164.46144865921042, 74.19457777154304, 196.07197384788262, 148.83074740907182, 35.933912583580586, 4.590239967603393, 78.14768567958139, 110.36291335292691, 126.13652638607229, 102.08287517826405, 160.43878104598747, 155.01462320273495, 67.50830142646367, 183.79802988079243, 144.80149095497507, 150.28757714218227, 48.61806052535338, 47.707916085822944, 179.05395502893774, 199.67585920624728, 153.8508334352389, 195.4705280983166, 106.4952855162857, 139.74138254146703, 196.89050976921618, 196.8216669188601, 187.95964975263473, 30.398417782741262, 126.9843505460811, 97.88524743968752, 179.2290075388831, 41.238747115942154, 9.772210446262463, 140.45453956679123, 158.18771871672735, 100.3420352743585, 91.27550816626642, 136.4812995782523, 99.85216119847652, 197.04603046491957, 193.6354375769893, 40.13974836539192, 101.84447268086676, 79.34546257459603, 1.2538574498785593, 127.5521468999901, 28.00330224013221, 28.210705820932258, 149.12923183901654, 182.57397351433607, 5.438864154495926, 83.91551043137977, 129.833153899724, 66.46201040325342, 196.00153817319847, 166.57774605846308, 197.89181334632565, 104.98315136918033, 31.630933824059014, 86.22731886677425, 194.45882975455228, 196.7901503222842, 192.3579055533893, 62.53200677426334, 169.39939195479448, 178.02013687952677, 103.69982133446112, 167.25569246832657, 146.74348267368546, 127.3566849783291, 95.07043853838636, 19.91864018633349, 124.48990552201113, 48.87157888911078, 77.80394686866828, 192.21202713746413]
l=[2, 7, 12, 12, 10, 9, 4, 9, 1, 11, 4, 6, 9, 10, 3, 6, 8, 2, 9, 5, 12, 4, 5, 10, 2, 9, 6, 2, 10, 5, 12, 1, 2, 4, 1, 1, 9, 11, 9, 10, 11, 5, 3, 11, 12, 5, 12, 2, 3, 5, 3, 8, 4, 7, 11, 2, 4, 10, 4, 12, 8, 7, 3, 11, 12, 7, 5, 1, 2, 2, 6, 6, 3, 11, 11, 3, 4, 9, 11, 8, 10, 8, 3, 8, 10, 11, 2, 5, 8, 7, 8, 2, 1, 1, 6, 10, 9, 2, 5, 4]
c=[40.889142732385785, 3.3835977348028417, 17.515508668055194, 7.316412598800724, 28.435875384024467, 40.51175232193015, 33.16652133210505, 16.291124538618085, 47.43421158681247, 37.63953829984323, 31.94357896336101, 35.44183045909062, 26.940631784561887, 29.78173320597273, 46.38573041710789, 43.23821584574432, 1.0487025803379297, 29.60706497878597, 2.527129183198319, 5.395107864032541, 46.455838217871985, 38.87316412042325, 35.08054778053921, 48.4168896845518, 3.825928851569861, 25.90422511056148, 23.2086873206898, 27.333732807408484, 16.59583007635799, 1.5600802032255852, 20.259357823398783, 48.88337336157257, 42.66218104433084, 28.404435232937125, 2.1091731494887855, 49.32514042252361, 5.10513471196991, 3.0983685254434388, 1.2110677187584116, 45.88972889502061, 25.35695437996399, 47.347041932677875, 44.55527805317549, 4.261475875111388, 48.340961557444984, 30.728152436147273, 33.06662654730123, 47.39049931374551, 29.525385174688665, 10.509422203453711, 30.189291093435283, 12.557306142045395, 34.631641475414, 12.988188003849496, 4.570539471600421, 33.33349830426613, 9.043953341551207, 12.5303533875695, 48.06409024180886, 27.607122654057413, 23.51095163030856, 49.58135710596629, 40.06220471750961, 29.34884712153401, 17.36301392056944, 44.66799171848997, 8.782713879787996, 40.76302182778369, 13.075606240134984, 46.05347919118508, 20.48427337696662, 29.569296743689502, 29.597663649037145, 29.94860080495593, 18.97343208570941, 2.3966468601158004, 27.106181759329196, 32.74607414955356, 38.76419409053098, 23.271717951768387, 28.321243366078765, 35.2837566557307, 45.01841384635872, 27.01800283777772, 41.57568790479618, 15.724256658935527, 17.231351635983152, 39.588276049260415, 9.482494502072251, 45.23785160546579, 7.769979086284839, 3.024180041347905, 36.255942940573675, 16.37048586358559, 10.526846551854138, 19.878303086663482, 32.84568726410923, 28.407907148980467, 36.603313221909, 48.985274728611124]
mindi=[6, 12, 12, 12, 11, 10, 8, 9, 3, 11, 12, 11, 12, 12, 3, 8, 10, 9, 12, 10, 12, 9, 10, 12, 7, 9, 8, 9, 12, 9, 12, 6, 4, 9, 3, 4, 11, 11, 12, 12, 12, 7, 10, 12, 12, 9, 12, 9, 10, 8, 10, 9, 11, 10, 12, 4, 5, 11, 12, 12, 12, 10, 8, 11, 12, 10, 8, 7, 5, 11, 10, 11, 8, 12, 11, 5, 10, 9, 12, 9, 10, 9, 3, 8, 11, 12, 9, 10, 11, 8, 11, 12, 11, 4, 9, 12, 12, 11, 11, 10];
maxdi=[10, 12, 12, 12, 11, 12, 12, 9, 10, 12, 12, 12, 12, 12, 5, 10, 12, 11, 12, 11, 12, 9, 12, 12, 9, 11, 12, 10, 12, 12, 12, 11, 6, 10, 7, 4, 12, 11, 12, 12, 12, 8, 10, 12, 12, 11, 12, 12, 10, 12, 11, 11, 11, 12, 12, 6, 12, 11, 12, 12, 12, 12, 8, 11, 12, 10, 10, 8, 12, 12, 12, 11, 10, 12, 12, 12, 11, 10, 12, 11, 12, 12, 3, 9, 11, 12, 10, 12, 11, 10, 11, 12, 11, 5, 11, 12, 12, 12, 11, 10];
maxsur=50.0
"""
#

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
    for i in sorted_indices:
        sol_instance.evalSol(i)
    return sol_instance

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
    for count in range(iterations):
        i = 0
        P_remaining = set(range(nOrders)) # set of indices of remaining profits to consider
        while P_remaining and i<nOrders:
            RCL = set()
            p_cota = p[sorted_indices[-1]] + alpha*(p[sorted_indices[i]]-p[sorted_indices[-1]])
            j = i
            while P_remaining and j < nOrders and p[sorted_indices[j]] >= p_cota:
                k,f = sol_instance.isFeasible(j)
                #print("is FEASIBLE K,F",(k,f))
                #print("j:",j)
                if k != -1:
                    RCL.add((j,f))
                    j = j + 1
                else:
                    if j in P_remaining: P_remaining.remove(j)
                while P_remaining and not (j in P_remaining) and j < nOrders: j = j + 1
            if RCL:
                m = random.choice(tuple(RCL)) # choose an element randomly from RCL
                sol_instance.insertion(m)
                P_remaining.remove(m[0])
            while P_remaining and not (i in P_remaining) and i < nOrders:
                i = i + 1

        local_search(sol_instance)

        if sol_instance.profit > best.profit:
            best = sol_instance.copy()

        # Print or use the resulting set S from the best solution
        print("GRASP", count,": Resulting set S:", best.S)
        print("GRASP", count,": Profit", best.profit)
        print("GRASP", count,": Used capacities", best.used_capacities)


    # Print or use the resulting set S from the best solution
    print("FINAL GRASP: Resulting set S:", best.S)
    print("FINAL GRASP: Profit", best.profit)
    print("FINAL GRASP: Used capacities", best.used_capacities)



def main():
    # Code for the main function
    print("This is the main function.")

    # Call the auxiliary function
    grasp(iterations=20,alpha=0.75)


# Call the main function if the script is executed
if __name__ == "__main__":
    main()
