def decimal_to_bin(n):
    if n == 0:
        return "0"

    bin = ""
    while n > 0:
        rest = n % 2
        bin = str(rest) + bin
        n = n // 2
    return bin


decimal_number = 14

print(f"{decimal_number} = {decimal_to_bin(decimal_number)}")
