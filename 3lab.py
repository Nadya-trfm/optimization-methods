from scipy.optimize import linprog
import numpy as np
from array import array

def is_int(n):
    return int(n) == float(n)

obj = [45, -65, 0, -2, 3]
#      ─┬  ─┬
#       │   └┤ Коэффициент для y
#       └────┤ Коэффициент для x
#       for x in range(0,21):
optsint = []
opts = []
neopt = []
for r in range(0, 21):
    for y in range(0, 21):
        for z in range(0, 21):

            A_ub_p = np.array([[-2,  0, y, 4, -3], [0.2,  0.8, 1.5, 0.9, z]])
            b_ub_p = np.array([-91, 26])
            A_eq_p = np.array([[15, r, 0, 34, -22], [1.8, -42, 6.4, 0, 3]])
            b_eq_p = np.array([56, 15])
            bnd = np.array([(0, float("inf")), (0, float("inf")),
                 (0, float("inf")),                    (0, float("inf")),
                   (0, float("inf"))])
            opt = linprog(c=obj, A_ub= A_ub_p, b_ub =b_ub_p,
            A_eq=A_eq_p, b_eq=b_eq_p, bounds=bnd, method="simplex")
            ds = [r, y, z]

            s = opt.fun
            if opt.message != 'Optimization terminated successfully.':
                print("Функция не оптимальна на", r, y, z)
            else:
                opts.append(opt.fun)
                if is_int(s):
                    print(r, y, z, opt.fun)
                    optsint.append(ds)
print("Минимальное значение функции:", min(opts))
print("Максимальное значение функции:", max(opts))
if 0 == len(optsint):
    print("Не существует такой набор параметров λ1, λ2, λ3, при которых задача линейного программирования имеет целочисленное решение.")
else:
    print(optsint)
