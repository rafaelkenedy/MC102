# f(x) = x2 −Y.
def raiz_newton(y):
    def f(x):
        return x ** 2 - y

    def f_derivada(x):
        return 2 * x

    x = y / 2

    for _ in range(100):
        estimativa = x - f(x) / f_derivada(x)

        if abs(estimativa - x) < 0.0000001:
            return estimativa

        x = estimativa
    return x


y = 25
result = raiz_newton(y)
print(result)
