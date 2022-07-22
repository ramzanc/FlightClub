# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)


def check_iata_empty():
    cities = []
    for dict in sheet_data:
        if dict["iataCode"] == "":
            cities.append(dict["city"])
    return cities


flight_search.import_empty_cities(check_iata_empty())
for dict in sheet_data:
    flight_search.return_iata(dict)

for destination in sheet_data:
    if flight_search.check_prices(destination["iataCode"]) is None:
        price, via = flight_search.return_one_stop(destination["iataCode"])
        notification_manager = NotificationManager()
        notification_manager.send_message(
            price=price,
            start_date=flight_search.today,
            end_date=flight_search.end_date,
            depart="London",
            arrival=destination["city"],
            stop_over=1,
            via=via
        )
    elif flight_search.check_prices(destination["iataCode"])<destination["lowestPrice"]:
        notification_manager = NotificationManager()
        notification_manager.send_message(
            price=flight_search.check_prices(destination["iataCode"]),
            start_date=flight_search.today,
            end_date=flight_search.end_date,
            depart="London",
            arrival=destination["city"]
        )
        pass

print(sheet_data)

data_manager.update_sheet_data(sheet_data)
