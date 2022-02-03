from scipy.optimize import minimize
import math
import numpy as np
import scipy.optimize as opt

def function(X):
    return X[0]**2+X[0]*X[1]+2*X[1]**2
x0 = np.zeros(2, dtype = float) # Вектор с двумя элементами типа float
# Начальная точка поиска минимума функции
x0[0] = -5.0
x0[1] = 5.0
xtol = 1.0e-05 # Точность поиска экстремума
res = opt.minimize(function,x0, method='nelder-mead'
                    #,options = {'xtol': xtol, 'disp': True}
                   )
print(res)