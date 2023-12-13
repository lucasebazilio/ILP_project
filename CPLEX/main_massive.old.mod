/*********************************************
 * OPL 22.1.0.0 Model
 * Author: adria y lucas
 * Creation Date: 30 nov. 2023 at 19:08:26
 *********************************************/

main {
	var src = new IloOplModelSource("Project.mod");
	var def = new IloOplModelDefinition(src);
	var cplex = new IloCplex();
	var ofile = new IloOplOutputFile("myout.csv");
	ofile.writeln("nOrders,Profit,Time")
	cplex.epgap=0.01;
	var iter = 5100;
	var start = cplex.getCplexTime();
	var end	= cplex.getCplexTime();
	while (iter <= 10000){
	  	var model = new IloOplModel(def,cplex);
		var filename = "instancesCPLEX/instance_n"+iter+"_t12_cplex.dat";
		var data = new IloOplDataSource(filename);
		model.addDataSource(data);
		model.generate();
		start = cplex.getCplexTime();
		if (cplex.solve()) {
		  /*
			ofile.writeln("Optimal Sol. with profit " + cplex.getObjValue() + "�");
			for (var i=1;i<=model.nOrders;i++) {
				if (model.y[i] == 1) ofile.writeln("{"+i+","+model.f[i],"}");
			}
		  */
		  end = cplex.getCplexTime();
		  ofile.writeln(model.nOrders,",",cplex.getObjValue(),",",end-start);
		}
		else {
			writeln("No solution found");
		}
		iter = iter + 100;
		if (end - start > 1800){
		  writeln("nOrders = "+iter+" passed the 30min time limit.")
		  iter = 10001;
		}
		writeln("Iter:", iter, " Time elapsed:", end-start)
	}		
	model.end();
	data.end();
	def.end();
	ofile.close();
	cplex.end();
	src.end();
};
