def find_solutions(c):
    for x1 in range(c + 1):
        for x2 in range(c - x1 + 1):
            x3 = c - x1 - x2
            print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")


c = 3
if c >= 0:
    find_solutions(c)
else:
    print("C be positive!")
