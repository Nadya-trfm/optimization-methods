from scipy.optimize import linprog
import numpy as np

obj = [45, -65, -2, 3]
#      ─┬  ─┬
#       │   └┤ Коэффициент для y
#       └────┤ Коэффициент для x
#       for x in range(0,21):
    #for y in range(0,21):
        #for z in range(0,21):
lhs_ineq = [[-2,  0, 0, 4, -3], [0.2,  0.8, 1.5, 0.9, 0]]  # левая сторона желтого неравенства

rhs_ineq = [-91, 26]# правая сторона желтого неравенства
lhs_eq = [[15, 0, 0, 34, -22], [1.8, -42, 6.4, 0, 3]] # левая сторона зеленого равенства
rhs_eq = [56, 15]     # правая сторона зеленого равенства
bnd = [(0, float("inf")),  # Границы x
                   (0, float("inf")),
                   (0, float("inf")),
                   (0, float("inf")),
                   (0, float("inf"))]  # Границы y
opt = linprog(c=0, A_ub=lhs_ineq, b_ub=rhs_ineq,
            A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
print(opt.x)
