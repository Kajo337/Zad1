
def func5(l: list, numb: int) -> bool:
    if numb in l:
        return 1
    else:
        return 0

print(func5([1,2,3,4,5],6))