import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_api_endpoint = "https://api.sheety.co/3ad4d65798307b6e81aeef85e93fcd21/flightDeals/prices"

    def get_sheet_data(self):
        self.response = requests.get(url=self.sheety_api_endpoint)
        response_json = self.response.json()
        self.sheet_data = response_json["prices"]
        return self.sheet_data

    def update_sheet_data(self, sheet):
        for i in range(0,len(sheet)):
            requests.put(url=f"{self.sheety_api_endpoint}/{i+2}", json={"price":sheet[i]})




