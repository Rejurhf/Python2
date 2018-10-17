# Rejurhf
# 02.10.2018

order_total = 247

# clasic if/else
if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total, discount)

print("Other way to do this:")

discountTernaty = 25 if order_total > 100 else 0
print(order_total, discount)
