def funcC(numbers):
    if len(numbers) != 10:
        print("Lista powinna zawierać dokładnie 10 liczb")
        return
    for i in range(len(numbers)):
        if (int(numbers[i])) % 2 == 0:
            print(numbers[i])

funcC(["2", "2", "3", "4", "8", "6", "7", "8", "9", "10"])