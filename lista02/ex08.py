valor = 0

fatorial = n = valor

if n >= 0:
    while n > 1:
        n = n - 1
        fatorial = fatorial * n

if fatorial > 0:
    print("O fatorial de", valor, "é igual a:", fatorial)
else:
    print("Não existe fatorial de", valor)
