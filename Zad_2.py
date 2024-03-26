from Klasy.Zad_2 import Library as lb, Employee as em, Order as o, Book as b

library1 = lb.Library("Los Angeles", "Sunset Boulevard", "90028", "10:00 AM - 8:00 PM", "+1 310-555-5678")
library2 = lb.Library("Chicago", "Michigan Avenue", "60611", "8:30 AM - 5:30 PM", "+1 312-555-9876")

book1 = b.Book(library1, "2021-08-15", "John", "Doe", 250)
book2 = b.Book(library2, "2023-03-20", "Emily", "Johnson", 400)
book3 = b.Book(library1, "2020-05-10", "Michael", "Brown", 180)
book4 = b.Book(library2, "2024-01-05", "Sarah", "Williams", 350)
book5 = b.Book(library1, "2022-11-30", "David", "Jones", 280)

employee1 = em.Employee("Alice", "Johnson", "2022-09-10", "1988-12-05", "Los Angeles", "Sunset Boulevard", "11-111", "111111111")
employee2 = em.Employee("Robert", "Williams", "2021-11-25", "1995-03-15", "Chicago", "Michigan Avenue", "22-222", "222222222")
employee3 = em.Employee("Emma", "Brown", "2023-03-05", "1992-07-20", "San Francisco", "Market Street", "33-333", "333333333")

order1 = o.Order(employee2, "John", [book2, book3], "2023-03-10")
order2 = o.Order(employee3, "Emily", [book4, book5, book1], "2023-04-05")

print(order1)
print(order2)
