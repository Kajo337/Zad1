def func3(numb: int) -> bool:
    if numb % 2 == 0:
        return 1
    else:
        return 0


even = func3(1)

if even:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')
