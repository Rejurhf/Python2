# Rejurhf
# 09.10.2018

from time import time
mx = 5000

t = time() # start time for the for loop
dmloop = []
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))
print('for loop: {:.4f} s'.format(time() - t)) # elapsed time

t = time() # start time for the comprehemsiom
dmlist = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f} s'.format(time() - t)) # elapsed time

t = time() # start time for the generator expression
dmgen = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t)) # elapsed time

print(dmloop == dmlist == dmgen, len(dmloop))
