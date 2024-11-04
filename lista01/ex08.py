year = 2008

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Ano bissexto!")
else:
    print("Não é bissexto!")
