from Klasy.Zad_3 import Property as p

class Flat(p.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat\n{super().__str__()}Floor: {self.floor}\n"