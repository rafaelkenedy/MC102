def is_even(numero):
    return numero % 2 == 0


def is_odd(numero):
    return numero % 2 != 0


def generate_games():
    games = []
    for n1 in range(1, 61):
        if not is_even(n1):
            continue
        for n2 in range(n1 + 1, 61):
            if not is_odd(n2):
                continue
            for n3 in range(n2 + 1, 61):
                if not is_even(n3):
                    continue
                for n4 in range(n3 + 1, 61):
                    if not is_odd(n4):
                        continue
                    for n5 in range(n4 + 1, 61):
                        if not is_even(n5):
                            continue
                        for n6 in range(n5 + 1, 61):
                            if not is_odd(n6):
                                continue
                            game = (n1, n2, n3, n4, n5, n6)
                            games.append(game)
    return games


print("Gerando todas as possibilidades de jogos supersticiosos da Mega-Sena...")
print("Atenção: Este processo pode levar alguns minutos devido ao grande número de combinações.\n")

todos_os_jogos = generate_games()

print(f"\nTotal de jogos possíveis: {len(todos_os_jogos)}")

if generate_games:
    print("\nAlguns exemplos de jogos gerados:")
    for i in range(min(10, len(todos_os_jogos))):
        print(todos_os_jogos[i])

else:
    print("Nenhum jogo pôde ser gerado com as condições especificadas.")
