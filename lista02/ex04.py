n = 10


def is_prime(number):
    divisors = 0
    for i in range(number, 0, -1):
        if number % i == 0:
            divisors += 1
    if divisors == 2:
        return True
    else:
        return False


def lower_prime(number):
    if (is_prime(number)):
        return number
    for i in range(number, 0, -1):
        if (is_prime(i)):
            return i


def upper_prime(number):
    while not is_prime(number):
        number += 1
    return number


def higher(number):
    if (is_prime(number)):
        return number
    for i in range(number, 0, -1):
        if (is_prime(i)):
            return i


print(lower_prime(n))
print(upper_prime(n))
