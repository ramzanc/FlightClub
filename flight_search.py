import requests
from flight_data import FlightData
import datetime as dt

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.cities = []
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.today = dt.datetime.today().strftime("%d/%m/%Y")
        self.end_date = (dt.datetime.now()+dt.timedelta(days=180)).strftime("%d/%m/%Y")
        self.kiwi_search_endpoint ="https://tequila-api.kiwi.com/v2/search"

    def import_empty_cities(self, cities):
        self.cities = cities

    def return_iata(self, dict):
        params = {
            "term": dict["city"]
        }
        header = {
            "apikey": "################",
        }
        response = requests.get(url=self.kiwi_endpoint, params=params, headers=header)
        response_data = response.json()
        if dict["city"] in self.cities:
            dict["iataCode"] = response_data["locations"][0]["code"]

    def check_prices(self, to_location):
        header = {
            "apikey": "###################"
        }
        params = {
            "fly_from": "LON",
            "fly_to": to_location,
            "date_from": self.today,
            "date_to": self.end_date,
            "curr": "GBP",
            "return_from": (dt.datetime.now() + dt.timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_to": (dt.datetime.now() + dt.timedelta(days=28)).strftime("%d/%m/%Y")
        }
        response = requests.get(url=self.kiwi_search_endpoint, params=params, headers=header)
        try:
            return response.json()["data"][0]["price"]
        except IndexError:
            return None

    def return_one_stop(self, to_location):
        header = {
            "apikey": "##################"
        }
        params = {
            "fly_from": "LON",
            "fly_to": to_location,
            "date_from": self.today,
            "date_to": self.end_date,
            "curr": "GBP",
            "return_from": (dt.datetime.now() + dt.timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_to": (dt.datetime.now() + dt.timedelta(days=28)).strftime("%d/%m/%Y"),
            "stop_overs": 1
        }
        response = requests.get(url=self.kiwi_search_endpoint, params=params, headers=header)

        price = response.json()["data"][0]["price"]
        via = response.json()["data"][0]["route"][0]["flyTo"]
        return price, via



    pass
