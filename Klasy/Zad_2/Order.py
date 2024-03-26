class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_info = "\n".join(f"    - {book}" for book in self.books)
        return f"Order:\nEmployee: {self.employee}\nStudent: {self.student}\nBooks:\n{book_info}\nOrder Date: {self.order_date}\n"