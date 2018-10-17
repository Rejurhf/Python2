# Rejurhf
# 10.10.2018

def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

print(list(fibonacci(500)))
