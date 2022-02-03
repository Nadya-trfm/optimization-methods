from scipy import optimize
import math
import numpy as np
import matplotlib.pyplot as plt


def scalar1(x):
    return 3 * x ** 4 - 3 * x ** 3 - 4 * x ** 2 - 1


def ravnomernyi_poisk(a, b):
    N = 1000
    xi = []
    fi=[]
    xi.append(a)
    fi.append(scalar1(a))

    for i in range(1, N+1):
        xi.append(a + i * ((b - a) / (N + 1)))
        fi.append(scalar1(xi[i]))

    mini=fi.index(min(fi))
    minimx=xi[mini]
    return minimx


def proverka_L(a, b, eps):
    L = abs(b - a)
    if L <= eps:
        return -1
    else:
        return 1

#работает
def delenie_otrezka(a, b):
    eps = 0.001
    x_srednee = (a + b) / 2
    k = 1
    while (k == 1):
        L = abs(b - a)
        y = a + L / 4
        z = b - L / 4
        f_sr = scalar1(x_srednee)
        f_y = scalar1(y)
        f_z = scalar1(z)
        if f_y < f_sr:
            b = x_srednee
            x_srednee = y
            k = proverka_L(a, b, eps)
        else:
            if f_z < f_sr:
                a = x_srednee
                x_srednee = z
                k = proverka_L(a, b, eps)
            else:
                a = y
                b = z
                k = proverka_L(a, b, eps)
    return x_srednee


def dihotomii(a, b):
    eps = 0.1
    l = 0.01
    k = 0
    #шаг3
    y = (a + b - l) / 2
    z = (a + b + l) / 2
    f_y = scalar1(y)
    f_z = scalar1(z)
    #step4
    if f_y <= f_z:
        b = z

    else:
        a = y
    #step5
    k=proverka_L(a,b,eps)
    if k == -1:
        xcz = (a + b) / 2
        return xcz
    else:
        #step3
        return dihotomii(a,b)

#работает
def zolotogo_sechenia(a, b):
    eps = 0.01
    y = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    z = a + b - y
    k = 1
    while (k == 1):
        f_y = scalar1(y)
        f_z = scalar1(z)
        if f_y <= f_z:
            b = z
            z = y
            y = a + b - y

            k = proverka_L(a, b, eps)
        else:
            a = y
            y = z
            z = a + b - z

            k = proverka_L(a, b, eps)
    xcz = (a + b) / 2
    return xcz


def fib(n):
    M = {0: 0, 1: 1}
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]


def fibonachii(a, b):
    l=0.01
    eps=0.001
    L = np.array((a, b))
    L[0] = a
    L[1] = b
    f = 1
    prev = 1
    N = 2
    k = 0
    while f <= (L[1] - L[0]) / l:
        temp = f
        f = f + prev
        prev = temp
        N = N + 1
        pass
    yk = L[0] + fib(N - 2) * (L[1] - L[0]) / fib(N)
    zk = L[0] + fib(N - 1) * (L[1] - L[0]) / fib(N)
    while k != N - 3:
        if scalar1(yk) <= scalar1(zk):
            L[1] = zk
            zk = yk
            yk = L[0] + fib(N - k - 3) * (L[1] - L[0]) / fib(N - k - 1)
        else:
            L[0] = yk
            yk = zk
            zk = L[0] + fib(N - k - 2) * (L[1] - L[0]) / fib(N - k - 1)
        k = k + 1
    yk = zk
    zk = yk + eps
    if scalar1(yk) <= scalar1(zk):
        L[1] = zk
    else:
        L[0] = yk
    return (L[1]+L[0])/2

xs = np.arange(-2,1,0.0001)
ys=scalar1(xs)
plt.plot(xs,ys)

result = optimize.minimize_scalar(scalar1, bounds=(-2, -0.3), method='Bounded')
print(result['x'])
print("равномерный",ravnomernyi_poisk(-2, -0.3))
print("деление отрезка", delenie_otrezka(-2,-0.3))
print("золотого сечения",zolotogo_sechenia(-2, -0.3))
print("дихотомии",dihotomii(-2,-0.3))
print("Фибоначи",fibonachii(-2, -0.3))
plt.show()