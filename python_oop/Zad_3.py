class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} sqm\nRooms: {self.rooms}\nPrice: ${self.price}\nAddress: {self.address}\n"
class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}Plot size: {self.plot} sqm\n"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return  f"Flat\n{super().__str__()}Floor: {self.floor}\n"


house = House(200, 7, 450000, "456 Elm Street", 500)
flat = Flat(80, 3, 150000, "789 Oak Street", 2)

print(house)
print(flat)
