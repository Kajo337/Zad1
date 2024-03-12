
def func6(l1: list, l2: list) -> list:
    l3 = set(l1 + l2)
    l4 = [x**3 for x in l3]
    return l4



print(func6([1,2,3,4],[3,4,5,6]))