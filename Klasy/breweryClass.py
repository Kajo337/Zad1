class Brewery:

    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.brewery_type = data.get('brewery_type')
        self.address_1 = data.get('address_1')
        self.address_2 = data.get('address_2')
        self.address_3 = data.get('address_3')
        self.city = data.get('city')
        self.state_province = data.get('state_province')
        self.postal_code = data.get('postal_code')
        self.country = data.get('country')
        self.longitude = data.get('longitude')
        self.latitude = data.get('latitude')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')
        self.state = data.get('state')
        self.street = data.get('street')

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nAddress: {self.address_1}, {self.city}, {self.state_province}, {self.postal_code}\nCountry: {self.country}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nPhone: {self.phone}\nWebsite: {self.website_url}\n"
