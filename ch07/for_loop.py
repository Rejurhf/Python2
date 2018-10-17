# Rejurhf
# 12.10.2018

class ExitLoopExeption(Exception):
    pass

# n = 100
# found = False
# for a in range(n):
#     if found: break
#     for b in range(n):
#         if found: break
#         for c in range(n):
#             if 42 * a + 17 * b + c == 5096:
#                 found = True
#                 print(a, b, c)

try:
    n = 100
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 42 * a + 17 * b + c == 5096:
                    raise ExitLoopExeption(a, b, c)
except ExitLoopExeption as ele:
    print(ele)
