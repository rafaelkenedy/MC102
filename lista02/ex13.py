def print_n_spaces(n):
    left = ""
    for i in range(1, n + 1):
        left += "* "
        right = "* " * (n - i)
        print(f"{left}+ {right}")

n = 6
print_n_spaces(n)
