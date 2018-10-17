# Rejurhf
# 09.10.2018

from math import sqrt, ceil

def get_primes(n):
    """Calculate a list of primes up to n (included). """
    primeList = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = int(ceil(sqrt(candidate)))
        for prime in primeList:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primeList.append(candidate)
    return primeList

print(get_primes(50))
