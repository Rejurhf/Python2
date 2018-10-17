# Rejurhf
# 26.09.2018

# 01
'''
late = False
if late:
    print('I need to call my manager!')
else:
    print('no need to call my manager...')
'''

# 02
income = 99000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print('I will pay:', income * tax_coefficient, 'in taxes\nMy income: ',
    income, '\nNetto: ', income * (1 - tax_coefficient))
