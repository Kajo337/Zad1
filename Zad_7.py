import Libs.requestsLib as requests
import Libs.argparseLib as argparse
import Klasy.breweryClass as Brewery


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
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', default=None)
    args = parser.parse_args()

    main(args.city)
