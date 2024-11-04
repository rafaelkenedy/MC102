import math

# a = int(input())
# b = int(input())
# c = int(input())

a = 4
b = 2
c = 1

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é equilátero!")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles!")
    else:
        print("O triângulo é escaleno!")

    s_p = (a + b + c) / 2
    t_area = math.sqrt(s_p * (s_p - a) * (s_p - b) * (s_p - c))
    print("Área do triângulo:", t_area)
else:
    print("Os valores informados não formam um triângulo!")
