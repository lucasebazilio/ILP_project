/*********************************************
 * OPL 22.1.0.0 Model
 * Author: adria
 * Creation Date: 29 nov. 2023 at 18:11:31
 *********************************************/
/*********************************************
 * OPL 22.1.0.0 Model
 * Author: Adria Lisa & Lucas Estevao
 * Creation Date: Nov 25, 2023 at 6:25:39 PM
 *********************************************/
// Input and range constants:
int nOrders = ...;
int nSlots = ...;
range N = 1..nOrders;
range T = 1..nSlots;
float p[i in N] = ...;
int l[i in N] = ...;
float c[i in N] = ...;
int mindi[i in N] = ...;
int maxdi[i in N] = ...;
float maxsur = ...;

// Model variables
dvar boolean x [i in N, j in T];
dvar boolean y [i in N];
dvar int f[i in N];
dvar boolean z[i in N, j in T];

// Objective function 
maximize (sum(i in N) y[i] * p[i]);

subject to {
  // Constraint 2, y definition
  forall(i in N) sum(j in T) x[i,j] >= y[i];

  // Constraint 3 surface constraint
  forall (j in T) sum(i in N) c[i]*x[i][j] <= maxsur;
  
  // Constraint 4 length constraint
  forall(i in N) sum (j in T) x[i][j] == l[i]*y[i];
  
  // Constraint 5 min finishing time 
  forall (i in N) f[i] >= y[i]*mindi[i];
  
  // Constraint 6 max finishing time
  forall (i in N) f[i] <= y[i]*maxdi[i];
  
  // Constraint 7 defining z 
  forall (i in N) z[i][1] == x[i][1];
  
  // Constraint 8 defining z
  forall(i in N, j in 2..nSlots) z[i][j] >= x[i][j] - x[i][j-1];

  // Constraint 9 defining z
  forall(i in N, j in 2..nSlots) z[i][j] >= x[i][j-1] - x[i][j];

  // Constraint 10 defining z
  forall(i in N, j in 2..nSlots) z[i][j] <= x[i][j] + x[i][j-1];

  // Constraint 11 defining z
  forall(i in N, j in 2..nSlots) z[i][j] <= 2 - x[i][j] - x[i][j-1];
 
  // Constraint 12 defining f
  forall (i in N, j in T) 1 + f[i] >= j*z[i][j];

  // Constraint 13 defining f
  forall (i in N) f[i] >= (2*y[i] - sum (j in T) z[i][j])*nSlots;
  
  // Constraint 14 defining f (and z)
  forall (i in N, j in T) 1 + f[i] <= j*z[i][j] + 
    (2 - sum(k in 1..j)z[i][k])*(nSlots + 1) + (1-z[i][j])*(nSlots+1);
}

 