print("Digite um número:")
# a = int(input())
a = 102

def is_less_than_100(n):
    return n < 100
def is_even(n):
    return n % 2 == 0


if is_less_than_100(a):
    if is_even(a):
        print("O número é par e menor do que 100")
    else:
        print("O número é ímpar e menor que 100")
else:
    if is_even(a):
        print("O número é par e maior ou igual do que 100")
    else:
        print("O número é ímpar e maior ou igual do que 100")