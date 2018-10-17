# Rejurhf
# 08.10.2018

def outer():
    test = 1

    def inner():
        test = 2

        def innerinner():
            global test
            test = 3
            print('innerinner:', test)

        innerinner()
        print('inner:', test)

    inner()
    print('outer:', test)

test = 0
outer()
print('global:', test)
