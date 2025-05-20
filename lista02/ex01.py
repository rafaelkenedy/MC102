def get_opt():
    return int(input())


while True:

    opt = get_opt()

    match opt:
        case 1:
            print("Pizza Marguerita")
        case 2:
            print("Pizza de Calabresa")
        case 3:
            print("Pizza de Pepperoni")
        case 4:
            print("Pizza de Mussarela")
        case 5:
            print("Sair")
            break
