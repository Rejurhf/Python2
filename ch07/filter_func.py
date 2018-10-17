# Rejurhf
# 12.10.2018

def filter_ints(v):
    # return [num for num in v if is_positive(num)]
    v = [num for num in v if num != 0]
    return [num for num in v if is_positive(num)]

def is_positive(n):
    return n > 0

print(filter_ints((5,3,-1,10,0)))
