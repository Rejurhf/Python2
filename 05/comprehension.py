# Rejurhf
# 09.10.2018

items = 'ABCDEF'
pairs = [(items[a], items[b])
    for a in range(len(items)) for b in range(a, len(items))]

print(pairs)
