# Rejurhf
# 09.10.2018

from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n+1), 1)

f = factorial(5)
print(f)
