def print_n_spaces(n):
    line = ""
    for i in range(1, n + 1):
        print(f"{line}{i}")
        line += " "


n = 6
print_n_spaces(n)
