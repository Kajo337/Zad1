
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = Student("Karol", [10, 20, 30, 40, 50, 60, 70])
student2 = Student("Michał", [50, 60, 70, 80, 90, 70, 70])

print(student1.is_passed())
print(student2.is_passed())
