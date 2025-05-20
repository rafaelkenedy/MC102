max = 6

lista = [1, 2, 9, 0, -3, 10]
# lista = [1, 2, 3, 4, 5, 9]

# for i in range(max):
#     lista.append(2)

print(lista)
is_ascending = True

# for i in range(max - 1):
#     actual = lista[i]
#     next = lista[i + 1]
#     if next < actual:
#         is_ascending = False
#         break

# list comprehension version
is_ascending = all(
    lista[i] <= lista[i + 1] for i in range(len(lista) - 1)
)

if is_ascending:
    print("Ascending!")
else:
    print("Not ascending!")
