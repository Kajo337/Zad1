def funcD(numbers):
    if len(numbers) != 10:
        print("Lista powinna zawierać dokładnie 10 liczb")
        return
    for i in range(1,len(numbers),2):
        print(numbers[i])


funcD(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])