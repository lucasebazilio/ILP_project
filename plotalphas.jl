using Plots, LaTeXStrings
using CSV
m = 200
pl = plot()
title!("Experiments for m = $m")
global M = [0 for i in 1:20]
for i in 1:7
    file = "experiments_m$m/pid$(i)_n5000_a100_m$m.csv"
    alpha = CSV.read(file, values; select = [1]) |> only
    p = CSV.read(file, values; select = [2]) |> only
    p = p.-minimum(p)
    global M = hcat(M, p)
    # Plotting the data
    pl = plot!(alpha, p, xlabel=L"$\alpha$", ylabel=L"Improvement on $\mathcal{S}.\texttt{totalProfit}$", label=false, linewidth=2)
end
println(M)
gp = groupedbar(alpha, M, bar_position = :stack, legend=false, xticks=[i/10 for i in 0:10])
display(gp)
