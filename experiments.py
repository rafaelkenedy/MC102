# # a = 3
# # b = 2
# # c = 1
# import math
#
# # a = 3.0
# # b = 6.0
# # operation = '+'
# #
# # if operation == '+':
# #     x = a + b
# # elif operation == '-':
# #     x = a - b
# # elif operation == '*':
# #     x = a * b
# # else:
# #     x = a / b
# #
# # print("Result: ", x)
#
# # paridade distinta
# # ok = (a % 2) != (b % 2)
# # confirmation = ((a + b) % 2) != 0
#
# print(ok)
# print(confirmation)
#
# # a = 3
# # b = 2
# # c = 1
# #
# # bridge = 0
#
# # if (a < b < c):
# #     min = a
# #     print(a)
# # elif (b < a < c):
# #     min = b
# #     print(b)
# # elif (c < b < a):
# #     min = c
# #     print(c)
# # else:
# #     print("O menor valor se repete portanto não há como definir um menor entre os 3!")
#
# # atribuição simultânea
# # if a > b:
# #     a, b = b, a
# # if a > c:
# #     a, c = c, a
# # if b > c:
# #     b, c = c, b
# #
# # print(a, b, c)
#
# # day = 1
# # month = 6
# # year = 2022
# #
# # day2 = 6
# # month2 = 1
# # year2 = 2022
#
# # if (year < year2):
# #     print("Data 1 ocorreu antes!")
# # elif (year2 < year):
# #     print("Data 2 ocorreu antes!")
# # elif (month < mouth2):
# #     print("Data 1 ocorreu antes!")
# # elif (mouth2 < month):
# #     print("Data 2 ocorreu antes!")
# # elif (day < day2):
# #     print("Data 1 ocorreu antes!")
# # elif (day2 < day):
# #     print("Data 2 ocorreu antes!")
# # else:
# #     print("As datas são iguais!")
# #
# # date1 = (year, month, day)
# # date2 = (year2, month2, day2)
# #
# # if date1 < date2:
# #     print("Data 1 ocorreu primeiro!")
# # elif date1 > date2:
# #     print("Data 2 ocorreu primeiro!")
# # else:
# #     print("As datas são iguais!")
#
#
# # a = 1
# # b = 12
# # c = -13
# #
# # if a != 0:
# #     delta = (b ** 2) - (4 * a * c)
# #     x_l = (-(b) + math.sqrt(delta)) / (2 * a)
# #     x_ll = (-(b) - math.sqrt(delta)) / (2 * a)
# #     print("x_l = ", x_l)
# #     print("x_ll = ", x_ll)
# # else:
# #     x = -(c/b)
# #     print("x = ", x)
#
#
# stone = "stone"
# paper = "paper"
# scissors = "scissors"
#
# player_a_choice = "Stone"
# player_b_choice = "paper"
#
# if player_a_choice == player_b_choice:
#     print("Tie")
# elif player_a_choice == stone and player_b_choice == scissors or \
#         player_a_choice == scissors and player_b_choice == paper or \
#         player_a_choice == paper and player_b_choice == stone:
#     print("Player A wins!")
# else:
#     print("Player B wins!")
from operator import indexOf

# a = 3
# b = 2
# c = 2

# if (a <= b) and (a <= c):
#     print(a)
# elif (b <= c):
#     print(b)
# else:
#     print(c)

# if a <= b and a <= c:
#     print(a)
# elif b <= c:
#     print(b)
# else:
#     print(c)


# print("Pedra = 0")
# print("Papel = 1")
# print("Tesoura = 2")
#
# jogadorA = int(input("Digite a primeira escolha: "))
# jogadorB = int(input("Digite a segunda escolha: "))
#
# resultado = (jogadorA  - jogadorB) % 3
#
# if resultado == 1:
#     print("O jogador A ganhou")
# elif resultado == 2:
#     print("O jogador B ganhou")
# else:
#     print("Empate")

# i = 1
# while i <= 100:
#     print(i)
#     i = i + 1

# n = 10
# while n >= 0:
#     print(n)
#     n = n - 1
#
# print("BOOM!")

# dividendo = 10
# divisor = 5
#
# quociente = 0
#
# while dividendo >= divisor:
#     print("Dividendo: ", dividendo)
#     print("Divisor: ", divisor)
#     print("Quociente: ", quociente)
#     dividendo = dividendo - divisor
#     quociente = quociente + 1
#
# print("Quociente Final: ", quociente)
# print("Rest: ", dividendo)

# base = 2
# exp = -2
#
# result = 1
#
# while exp > 0:
#     result = result * base
#     exp = exp - 1
#
# while exp < 0:
#     result = result / base
#     exp = exp + 1
#
# print(result)

# n = 0
# ok = True
#
# while ok:
#     x = int(input("Entre com um número inteiro positivo: "))
#     if x > 0:
#         n = n + 1
#     else:
#         ok = False
# print("Quantidade de números positivos fornecidos: ", n)

# n = int(input("Entre com um número inteiro positivo: "))
# fat = 1
# i = 2
#
# while n > 1:
#     fat = fat * n
#     n = n - 1
#
# print("Resultado:", fat)

# lista = [40, 3, 61, 7, 3]
#
# print(lista)
#
# lista_mista = ["Gato", 42, True, 5.4, "Cachorro", 73]
# #
# # print(lista_mista)
# #
# # print(lista[0])
# # print(lista_mista[0])
# #
# # print(lista[-1])
# # print(lista_mista[-2])
#
# i = 0
# while i < len(lista):
#     print(lista[i])
#     i += 1

# numeros = [3, 1, 7, 9, 4]
# maximo = 0
#
# i = 0
# while i < len(numeros):
#     if numeros[i] > maximo:
#         maximo = numeros[i]
#     i += 1
#
# i = 0
# while i < len(numeros):
#     if numeros[i] > maximo:
#         maximo = numeros[i]
#     i += 1
#
#
# print(maximo)

# a = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]
#
# soma = 0
#
# for linha in a:
#    for elemento in linha:
#       soma += elemento
#
# print(soma)

# a = (1, 2, 3, 4, 5)
# b = [1, 2, 3, 4, 5]
#
# print(type(a))
# print(type(b))

# name = "Rafael"
#
# for letra in name:
#     print(letra)

# letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#           "x", "w", "y", "z"]
#
# for letra in letras:
#     print(letra)

# numeros = [3, 1, 7, 9, 4]
# maximo = 0
#
# for numero in numeros:
#     if numero > maximo:
#         maximo = numero
#
# print(maximo)
#
# print(list(range(2, 6)))
# print(list(range(1, 5)))
# print(list(range(0, 4)))
# print(list(range(4)))
# print(list(range(2, 10, 2)))
# print(list(range(1, 15, 3)))

# print(type(range(10)))

# n = 10
# potencia = 1
#
# for i in range(n):
#     potencia = potencia * 2
#     print(potencia)

# n = 10
# fatorial = 1
# for i in range(n, 0, -1):
#     fatorial = fatorial * i
# print(fatorial)

# x = int(input("Digite um número: "))
# for i in [2, 4, 7, 1, 0, 8, 9, 5]:
#     print("Verificando elemento", i)
#     if i == x:
#         print("Elemento", i, "encontrado!")
#         break

# for i in  range(1, 10):
#     if i == 5:
#         break
# print(i)
# print("Fim do programa!")


# n = 0
#
# while True:
#     x = int(input("Entre com um número inteiro positivo:"))
#     if x <= 0:
#         break
#     n = n + 1
# print("Quantidade de números positivos fornecidos: ", n)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# print("Fim do programa!")


# for i in range(0, 10):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(0, 20):
#     if i % 2 == 1:
#         continue
#     print(i)

# n = 8
# i = n
# while i >= 1:
#     if (n % i) == 0:
#         print("Divisor: ", i)
#     i -= 1
#
# n = 8
# i = n
# c_divisores = 0
# while i >= 1:
#     if (n % i) == 0:
#         c_divisores += 1
#     i -= 1
#
# print("Qtd. divisores: ", c_divisores)


# n = 11
# i = n
# c_divisores = 0
# while i >= 1:
#     if (n % i) == 0:
#         c_divisores += 1
#     i -= 1
#
# if c_divisores == 2:
#     print("O número", n, "é primo")
# else:
#     print("O número", n, "NÃO é primo")
#
#
# n = 210

# n = 210
# fator = 2
# while n > 1:
#     while n % fator == 0:
#         print(fator)
#         n //= fator
#     fator += 1

# n = 350
# fator = 2
#
# fatores = set()
#
# while n > 1:
#     while n % fator == 0:
#         fatores.add(fator)
#         print(f"fator: {fator}, n antes: {n}", end=" -> ")
#         n //= fator
#         print(f"n depois: {n}")
#     fator += 1
#     print("fator: ", fator)
#
# print(f"Fatores únicos: {fatores}")

# n = 120
# cont = 0
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         cont += 1
#
# print(cont)

# n = 300
# divisor = 2
#
# while n != 1:
#     if n % divisor == 0:
#         print(divisor)
#         n = n // divisor
#     else:
#         divisor = divisor + 1

# for i in range(1, 11):
#     print("Tabuada do ", i, ":", sep = "")
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

# n = 10
# m = 10
#
# intervalo = range(10, 3)
#
# print(type(intervalo))
# for i in range(n):
#     print("#" * m)

# n = 10
#
# for i in range(1, n+1):
#     for j in range(i):
#         print('#', end = "")
#     print()

# for h in range(24):
#     for m in range(60):
#         print(h, m, sep = ":")

# for h in range(24):
#     for m in range(60):
#         print('{:02d}:{:02d}'.format(h, m))
#
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             print('{:02d}:{:02d}:{:02d}'.format(h, m, s))

# n = 5
#
#
# for j in range(1, n + 1):
#     soma = 0
#     for i in range(1, j + 1):
#         soma += i
#     print(soma)

# for g in range(1, 500):
#     for i in range(1, 10+1):
#         print("x" * i, " " * int(g / 10), "x" * (10 - i))
#     for j in range(10+1, 1, -1):
#         print("x" * j, " " * int(g / 10), "x" * (10 - j))

# import time
# import os
#
# for g in range(1, 500):
#     for i in range(1, 11):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print("x" * i + " " * (g % 10) + "x" * (10 - i))
#         time.sleep(0.05)
#     for j in range(10, 0, -1):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print("x" * j + " " * (g % 10) + "x" * (10 - j))
#         time.sleep(0.05)

#
# n = 5
#
# for j in range(1, n + 1):
#     soma = 0
#     for i in range(1, j + 1):
#         soma = soma + (2 * i - 1)
#     print(soma)

# frutas = ["Abacaxi", "Banana", "Caqui", "Damasco", "Embaúba", "Figo", "Graviola"]
# dados = ["Rafael", 34, True, "Pedro", "Ana", 1.78, 2001]
#
# print(frutas)
# print(dados)
#
# print(list(range(10)))
# print(list())
# print(list(["Toyota", "Volkswagen", "Ford"]))
#
# unicamp = list("Unicamp")
# print(unicamp)
#
# listaVazia = []
# print(listaVazia)

# x = list(2) 'int' object is not iterable
# print(x)
#
# letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
# print(letras[0])
# print(letras[1])
# print(letras[4])
#
# print(letras[-1])
# print(letras[-2])
# print(letras[-3])
# print(len(frutas))
# print(frutas.__len__())

# lista[start:stop:step]

# print(letras[1:4:1])
# print(letras[1:4])
# print(letras[:3])
# print(letras[-4:])
# print(letras[-4::1])
# print(letras[::2])
# print(letras[:10:])
# print(letras[9::])
# print(letras[-10::])
# print(letras[1::2])
# print(letras[::-1])

# empresas = ["Apple", "Samsung", "Microsoft", "Google", "OpenAI"]
# empresas[2] = "Meta"
#
#
# print(empresas)

# lista = [0, 1, 2, 3, 4, 5]
# print(lista)
# lista[2:4] = ["A", "B"]
# print(lista)
#
# lista = [0, 1, 2, 3, 4, 5]
# print(lista)
# lista[2:4] = [8, 8, 8]
# print(lista)

# letras = list("ABCDEF")
# numeros = list(range(6))
#
# print(letras)
# print(numeros)
#
# letras[2:4], numeros[2:4] = numeros[2:4], letras[2:4]
# print(letras)
# print(numeros)
#
# x = 0
# y = 1
# print(x, y)
# x, y = y, x
# print(x, y)
#
# lista = [0, 1, 2, 3, 4, 5]
# print(lista)
# lista[4:6] = []
# print(lista)

# top5 = ["Black Mirror", "Breaking Bad", "Friends", "Game of Thrones", "The Big Bang Theory"]
# print("House MD" in top5)
# print("Game of Thrones" in top5)

# animais = []
# animais.append("Gato")
# print(animais)
# animais.append("Cachorro")
# print(animais)
#
# frutas = ["Abacaxi", "Banana", "Damasco"]
# frutas.insert(2, "Caqui")
# frutas.insert(len(frutas), "Manga")
#
# print(frutas)

# n = int(input("Quantos númoeros serão lidos? "))
# lista = []
# for i in range(n):
#     lista.append(int(input()))
# x = int(input("Qual o número a procurar? "))
# if x in lista:
#     print(x, "pertence à lista")
# else:
#     print(x, "não pertence à lista")

# lista = []
#
# keep = True
#
# while keep:
#     number = int(input("Enter a number: "))
#     if number >= 0:
#         lista.append(number)
#     else:
#         keep = False
# print(lista)
# print("Fim do programa!")

lista = []

# keep = True

# while True:
#     number = int(input("Enter a number: "))
#     if number >= 0:
#         lista.append(number)
#     else:
#         break
# print(lista)
# print("Fim do programa!")

# cinema = ["Sony Pictures", "Walt Disney", "Universal Pictures", "Warner"]
# if "Disney" in cinema:
#     print(cinema.index("Disney"))
# else:
#     print("Disney não está na lista.")

# paises = ["Argentina", "Brasil", "Canadá", "Dinamarca"]
# paises.remove("Argentina")
# print(paises)
#
# if "Dinamarca" in paises:
#     paises.remove("Dinamarca")
# else:
#     print("Dinamarca não está em países!")
# print(paises)
#
# print(paises.pop(1))
# print(paises)
#
# mentos = ["Morango", "Laranja", "Menta", "Banana"]
# x = mentos.pop(1)
# print(x)
# print(mentos)
#
# paises = ["Brasil", "brasil", "Brazil", "Brasil"]
#
# print(paises.count("brazil"))

# n = int(input("Quantos números lidos? "))
#
# lista = []
# for i in range(n):
#     lista.append(int(input()))
#
# x = int(input("Qual o número deve removido? "))
# c = lista.count(x)
# for i in range(c):
#     lista.remove(x)
#
# print(lista)

# n = int(input("Quantos números serão lidos? "))
#
# lista = [int(input()) for i in range(n)]
#
# x = int(input("Qual o número deve ser removido? "))
#
# lista = [i for i in lista if i != x]
#
# print(lista)

# semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
# print(semana)
#
# semana.reverse()
#
# print(semana)

# a = [5, 3, 1, 4, 2, 6]
# a.sort()
# print(a)
#
# a.reverse()
# print(a)
#
# a.sort(reverse = True)
# print(a)

# a = [5, 3, 1, 4, 2, 6]
# b = sorted(a)
# b.reverse()
# print(sorted(a)[::-1])
# print(a)


# a = [1]
# b = a
# b.append(2)
# c = b
#
# c.append(3)
# print(a)


# a = [1]
# b = a.copy()
# b.append(2)
# c = b.copy()
# c.append(3)
# print(a)
# print(b)
# print(c)

# a = [1]
# b = a[:]
# b.append(2)
# c = list(b)
# c.append(3)
# print(a)
# print(b)
# print(c)


# a = [1]
# b = a[:]
# b.append(2)
# c = list(b)
# c.append(3)
# print(a)
# print(b)
# print(c)

# a = [1, 2]
# b = [3, 4]
# c = [5, 6]
# print(a + b + c)
#
# print(c + b + a)
#
# print( b + c + a)

# a = [1]
# b = a + [2]
# print(a)
# print(b)

# numeros = [2.14, 5.32, 2.45, 1.43, 3.27]
# print(min(numeros))
#
# print(max(numeros))
#
# print(sum(numeros))
#
# vingadores = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]
# print(vingadores)
# vingadores.append("Homem Aranha")
# print(vingadores)
#
# if "Thor" in vingadores:
#     print(vingadores.index("Thor"))
#
# vingadores.remove("Viúva Negra")
# vingadores.remove("Homem de Ferro")
#
# print(vingadores)

# v1 = []
# v2 = []
#
# n = 12345678


# l1 = [7, 2, 9]
# l2 = [2, 5, 1, 3]
# l3 = l1 + l2
#
# l3.sort()
# print(l3)
#
# l3.reverse()
# print(l3)
































