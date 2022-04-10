from numba import njit
import random


@njit
def f(x):
    return x ** 5 - 3 * x ** 3 + 7 * x ** 2 - 1


@njit
def primitive(x):
    return x ** 6 / 6 - 3 / 4 * x ** 4 + 7 / 3 * x ** 3 - x


@njit
def montecarlo(l, r, N):
    res = 0
    deltax = (r - l) / N
    for i in range(N):
        ksi = random.random()
        x = ksi * deltax + l + i * deltax
        res += f(x)
    return res * deltax


@njit
def newtonleibliz(l, r):
    return primitive(r) - primitive(l)


left = float(input('Введите левую границу:'))
right = float(input('Введите правую границу:'))
N = int(input('Введите число точек (чем больше, тем точнее, но дольше работает :) )'))

print('Интеграл, вычисленный методом Монте-Карло:', montecarlo(left, right, N))
print('Интеграл, вычисленный по формуле Ньютона-Лейбница:', newtonleibliz(left, right))
print('Точность метода Монте-Карло:', 100 * min((montecarlo(left, right, N) / newtonleibliz(left, right),
                                                 newtonleibliz(left, right) / montecarlo(left, right, N,
                                                                                         ))), '%')
