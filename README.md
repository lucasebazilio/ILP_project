# Lucas' & Adrià's Repository of Algorithmic Methods for Mathematical Models

This repository includes the work we made for the course AMMM assignment at our master's degree. We provide 4 different methods for solving the same problem, about scheduling for a bakery, and a comparative study. The details about the problem can be read at assignment.pdf

## Generate Problem Instances
The format of the instances is slightly different for CPLEX and the Heuristic solvers in python. To than end, we provide the scripts "instanceGen..." to generate instance for each or both these formats.
We include all the instances used in the report for reproductibility, but if you want to run any new instance with any of the methods, pleace place in a similar directory route.

## Linear Programing with CPLEX
The file Project.mod contains our Integer Linear Programming formulation for IBM CPLEX, a commercial linear optimization solver.
- **Basic Execution**: One should first try to run it with the data instance smallinstance.dat in a run configuration, you will be able to see the results as the values of the model variables described in our report.pdf.
- **Comparative Study**: to replicate our results just run main_massive.mod and it will produce a .csv file with the total profit and execution time for all the instances in the instancesCPLEX subdirectory.

Finally, note that we used different names for the input variables than the ones proposed by our teachers. We apologize if that leads to any confusion.

## Heuristic Algorithms:
We implemented three algorithms in python that produce non-optimal but fast solution to the problem, namely, a *Greedy*, *Greedy + Local Search* and *GRASP*. They are located inside the "algorithms" directory.
- **Basic execution**: Just run the scripts any of the scripts greedy.py, greedyLocal.py or grasp.py. You can select the instance of the problem that we want to solve by modifieng the variable "dat_file" present in all three scripts. 

- **Solving multiple instances**: The scrips evalGreedy.py, evalLocal.py and evalGrasp.py generate a .csv with the solutions and computation times for each instance from $n = 100$ to $n = 5100$ for their respective heuristic algorithm. It is of paramount importance to have these instances in the directory *instancesPython*, precisely as it is defined in the implementations.

## Reproducing our plots 
We used the jupyter notebook "Plot_maker.ipynb" to generate all the plots used in the report. Before describing the structure of the notebook, the first step is to load the following files in our notebook environment: 
 - average_profits_n5000_m20.csv
 - average_profits_n5000_m60.csv
 - comparative_Greedy.csv
 - comparative_LocalSearch.csv
 - comparative_cplex.csv
 - comparative_Grasp_m20_alpha02.csv
 - comparative_Grasp_m60_alpha015.csv 

The notebook is structured in two sections:
  - **Alpha Tuning**: In this section, we perform the experiments necessary for the tuning of the alpha parameter in the GRASP algorithm for $m = 20$ and $m = 60$ iterations.
  - **Comparative Analysis**: In this section we perform a comparative analysis between CPLEX and the metaheuristics algorithms. Both in terms of quality of the solutions and computation time. We also compare the GRASP algorithm with different values of the number of
    iterations and *m* and tuned $\alpha$.