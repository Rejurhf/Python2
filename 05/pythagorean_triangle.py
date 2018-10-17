# Rejurhf
# 09.10.2018

from math import sqrt

max = 10
legs = [(a, b, sqrt(a ** 2 + b ** 2))
    for a in range(1, max) for b in range(a, max)]
legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]
print(legs)
