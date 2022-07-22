import requests
from twilio.rest import Client
import os
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_api_key = "bd9e25223a4723245e04f88ebef4847b"
        self.account_sid = "AC3df3d2800bbf6387453c357d7a87326c"
        self.auth_token = '89c7f1963cddbb4fef6515b3d6829651'

    def send_message(self, price, depart, arrival, start_date, end_date, stop_over=0, via=""):
        client = Client(self.account_sid, self.auth_token)
        if stop_over == 0:
            message = client.messages.create(
                from_="+18065421404",
                to="+917561824387",
                body=f"Low price alert! Only £{price} to fly from {depart} to {arrival}, from {start_date} to {end_date}"
            )
        else:
            message = client.messages.create(
                from_="+18065421404",
                to="+917561824387",
                body=f"Low price alert! Only £{price} to fly from {depart} to {arrival}, from {start_date} to {end_date}\nFlight has {stop_over} stop over, via {via}"
            )
