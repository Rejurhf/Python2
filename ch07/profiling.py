# Rejurhf
# 12.10.2018

def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples

def calc_hypotenuse(a, b):
    return (a**2 + b**2) ** .5  #improve performence:
    # return (a**a + b**b) ** .5

def is_int(n):
    return n.is_integer() # as above
    # return n == int(n)

triples = calc_triples(1000)

# python3 -m cProfile ch07/profiling.py
