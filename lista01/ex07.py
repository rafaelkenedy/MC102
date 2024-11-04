# opt = character(input())
# tempeture = character(input())

opt = 'C'
in_tempeture = 32

if opt == 'F':
    c = 5 / 9 * (in_tempeture - 32)
    print("Temperatura em Celsius: ", c)
else:
    f = in_tempeture * 9 / 5 + 32
    print("Temperatura em Fahrenheit: ", f)
