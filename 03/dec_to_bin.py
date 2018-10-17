# Rejurhf
# 02.10.2018

n = 39
remainders = []
while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2

# reverse list
remainders = remainders[::-1]
print(remainders)

# more pythonic way to do this
n2 = 39
remainders2 = []
while n2 > 0:
    n2, remainder2 = divmod(n2, 2)
    remainders2.append(remainder2)

remainders2 = remainders2[::-1]
print(remainders2)
