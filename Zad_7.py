import requests
import argparse


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


def main(city=None):

    params = {}
    breweries_list = []

    if city:
        url = "https://api.openbrewerydb.org/v1/breweries?by_city={city}"
    else:
        url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

    if city:
        response = requests.get(url, params=city)
    else:
        response = requests.get(url)
    if response.status_code == 200:
        breweries_data = response.json()
        data_list = [Brewery(data) for data in breweries_data]

        breweries_list.append(data_list)

    else:
        print("Nie udało się pobrać danych z API.")
    for brewery in breweries_list:
        for data in data_list:
            print(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch breweries from Open Brewery DB API')
    parser.add_argument('--city', default=None)
    args = parser.parse_args()

    main(args.city)
