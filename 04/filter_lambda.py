# Rejurhf
# 09.10.2018

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

print(get_multiples_of_five(50))

# more lambda's
#adder
def adder(a, b):
    return a + b

adder_lambda = lambda a, b: a + b

# to uppercase
def to_uppercase(str):
    return str.upper()

to_uppercase_lambda = lambda s: s.upper()    
