from Klasy.Zad_3 import Property as p

class House(p.Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}Plot size: {self.plot} sqm\n"

