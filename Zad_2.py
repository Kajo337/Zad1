
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen Hours: {self.open_hours}\n Phone: {self.phone}\n"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\nHire Date: {self.hire_date}\nBirth Date: {self.birth_date}\nCity: {self.city}\nStreet: {self.street}\n"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\nPublication Date: {self.publication_date}\nNumber of Pages: {self.number_of_pages}\nLibrary: {self.library}\n"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_info = "\n".join(f"    - {book}" for book in self.books)
        return f"Order:\nEmployee: {self.employee}\nStudent: {self.student}\nBooks:\n{book_info}\nOrder Date: {self.order_date}\n"


library1 = Library("Los Angeles", "Sunset Boulevard", "90028", "10:00 AM - 8:00 PM", "+1 310-555-5678")
library2 = Library("Chicago", "Michigan Avenue", "60611", "8:30 AM - 5:30 PM", "+1 312-555-9876")

book1 = Book(library1, "2021-08-15", "John", "Doe", 250)
book2 = Book(library2, "2023-03-20", "Emily", "Johnson", 400)
book3 = Book(library1, "2020-05-10", "Michael", "Brown", 180)
book4 = Book(library2, "2024-01-05", "Sarah", "Williams", 350)
book5 = Book(library1, "2022-11-30", "David", "Jones", 280)

employee1 = Employee("Alice", "Johnson", "2022-09-10", "1988-12-05", "Los Angeles", "Sunset Boulevard", "11-111", "111111111")
employee2 = Employee("Robert", "Williams", "2021-11-25", "1995-03-15", "Chicago", "Michigan Avenue", "22-222", "222222222")
employee3 = Employee("Emma", "Brown", "2023-03-05", "1992-07-20", "San Francisco", "Market Street", "33-333", "333333333")

order1 = Order(employee2, "John", [book2, book3], "2023-03-10")
order2 = Order(employee3, "Emily", [book4, book5, book1], "2023-04-05")

print(order1)
print(order2)
