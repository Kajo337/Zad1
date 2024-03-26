from Klasy.Zad_2 import Student as st

student1 = st.Student("Karol", [10, 20, 30, 40, 50, 60, 70])
student2 = st.Student("Michał", [50, 60, 70, 80, 90, 70, 70])

print(student1.is_passed())
print(student2.is_passed())
