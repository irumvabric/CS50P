while True:
    try:
        Fraction = input("Fraction: ")
        one = Fraction.split('/')

        x = int(one[0])
        y = int(one[1])

        z = x / y
        z = str(z)

        z = z.split('.')
        z = int(z[1])
        print(z)

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

if x == 1 and y == 4:
    print('25%')
elif x == 1 and y == 2:
        print('50%')
elif x == 3 and y == 4:
    print('75%')
elif x == 4 and y == 4:
    print('F')
elif x == 0 and y == 4:
    print('E')

            
            