def funcB(numbers):
    if len(numbers) != 5:
        print("Lista powinna zawierać dokładnie 5 liczb")
        return
    print("Oto lista liczb pomnożonych przez 2")
    for number in numbers:
        print(int(number)*2)
    changed_numbers = [int(number)*2 for number in numbers]
    print(changed_numbers)

funcB(["1", "2", "3", "5", "10"])