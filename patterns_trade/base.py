from requests import Session

class Base_binance():

    def __init__(self) -> None:
        self.session = Session()
        self.headers = {
         'Accepts': 'application/json'
        }