m = 270
n = 192


def mdc(a, b):
    if a == 0 and b == 0:
        return "Indefinido"
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(mdc(m, n))


def mdc_old(a, b):
    if a == 0 and b == 0:
        return "Indefinido"
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return abs(a)

print(mdc_old(m, n))