# Rejurhf
# 02.10.2018

people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)


# other way
# people = ['Jonas', 'Julio', 'Mike', 'Mez']
# ages = [25, 30, 31, 39]
# nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
# for data in zip(people, ages, nationalities):
#     person, age, nationality = data
#     print(person, age, nationality)
