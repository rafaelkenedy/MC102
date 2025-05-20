lista = {2, 61, -1, 0, 88, 55, 3, 121, 25, 75}

# print(lista)

intervalo_a = 0
intervalo_b = 0
intervalo_c = 0
intervalo_d = 0


def count_members_in(init, end):
    qtd = 0
    for i in lista:
        if init <= i <= end:
            qtd += 1
    return qtd


print("[0, 25]:", count_members_in(0, 25))
print("[26, 50]:", count_members_in(26, 50))
print("[51, 75]:", count_members_in(51, 75))
print("[76, 100]:", count_members_in(76, 100))
