"""List of prime numbers generator."""


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    list = []
    num = 2
    while len(list) < number_of_primes:
        primeFlag = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                primeFlag = False
        if primeFlag:
            list.append(num)
        num += 1
    return list
