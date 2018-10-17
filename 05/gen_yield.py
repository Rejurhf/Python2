# Rejurhf
# 09.10.2018

def geometric_progresion(a, q):
    k = 0
    while True:
        result = a * q**k
        if result < 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progresion(2, 5):
    print(n)
