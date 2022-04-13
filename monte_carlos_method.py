# Определенный интеграл полинома
import random

coefs = list(map(int, input('Введите коэффициенты полинома по убыванию степени мономов:').split()))


def f(x, m):
    res = 0
    for i in range(len(m)):
        res += x ** (len(m) - i - 1) * m[i]
    return res


def primitive(x, m):
    m1 = []
    for i in range(len(m)):
        m1.append(m[i] / (len(m) - i))
    m1.append(0)
    return f(x, m1)


def montecarlo(l, r, N, m):
    res = 0
    deltax = (r - l) / N
    for i in range(N):
        ksi = random.random()
        x = ksi * deltax + l + i * deltax
        res += f(x, m)
    return res * deltax


def newtonleibliz(l, r, m):
    return primitive(r, m) - primitive(l, m)


left = float(input('Введите левую границу:'))
right = float(input('Введите правую границу:'))
N = int(input('Введите число точек (чем больше, тем точнее, но дольше работает :) )'))

print('Интеграл, вычисленный методом Монте-Карло:', montecarlo(left, right, N, coefs))
print('Интеграл, вычисленный по формуле Ньютона-Лейбница:', newtonleibliz(left, right, coefs))
print('Точность метода Монте-Карло:', 100 * min((montecarlo(left, right, N, coefs) / newtonleibliz(left, right, coefs),
                                                 newtonleibliz(left, right, coefs) / montecarlo(left, right, N,
                                                                                                coefs))), '%')
