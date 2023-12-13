/*********************************************
 * OPL 22.1.0.0 Model
 * Author: Adria Lisa & Lucas Estevao
 * Creation Date: Nov 25, 2023 at 6:25:39 PM
 *********************************************/


int nOrders = ...;
int nSlots = ...;
float maxsur = ...;
range N = 1..nOrders;
range T = 1..nSlots;
dvar boolean x [i in N, j in T];
dvar boolean y [i in N];
dvar boolean andCondition[i in N, j in T];
//dvar int xt[i in N];
dvar boolean z[i in N, j in T];
//dvar int mindi[i in N];
//dvar int maxdi[i in N];
float p[i in N] = ...;
int l[i in N] = ...;
int mindi[i in N] = ...;
int maxdi[i in N] = ...;

float c[i in N] = ...;



// Objective
maximize (sum(i in N) y[i] * p[i]);

subject to {

  // Constraint 1
  // The total surface of taken orders does not exceed the maximum surface
  forall (j in T) sum(i in N) c[i]*x[i][j] <= maxsur;

  // Constraint 2.1
  // The start time for each order is within valid time slots
  forall (i in N) l[i]*y[i]+(sum(j in T) andCondition[i][j]) >= y[i]*mindi[i];

  // Constraint 2.2
  forall (i in N) l[i]*y[i]+(sum(j in T) andCondition[i][j]) <= y[i]*maxdi[i] + (1-y[i])*nSlots;

  // Constraint 3
  // The start time is correct
  forall(i in N) forall(j in T) {
    andCondition[i][j] >= 1 - j + sum(k in 1..j) (1 - x[i][k]);
  		forall(k in 1..j) andCondition[i][j] <= (1-x[i][k]);
  }


  // Constraint 4
  // y definition
  forall(i in N) sum(j in T) x[i,j] >= y[i];

  // Constraint 5
  forall (i in N) sum (j in T) z[i][j] <= 2;

  // Constraint 6
  forall(i in N) sum (j in T) x[i][j] == l[i]*y[i];

  // Constraint 7
  forall(i in N, j in 2..nSlots) z[i][j] >= x[i][j] - x[i][j-1];

   // Constraint 8
  forall(i in N, j in 2..nSlots) z[i][j] >= x[i][j-1] - x[i][j];

  // Constraint 9
  forall(i in N, j in 2..nSlots) z[i][j] <= x[i][j] + x[i][j-1];

   // Constraint 10
  forall(i in N, j in 2..nSlots) z[i][j] <= 2 - x[i][j] - x[i][j-1];

  // Constraint 11
  forall (i in N) z[i][1] == x[i][1];



}


// Post-processing
execute {


};

